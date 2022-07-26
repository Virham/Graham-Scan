# https://en.wikipedia.org/wiki/Graham_scan

import pygame
import random
import math
import time
import json


from Triangulation import Triangulation

class Main:
    def __init__(self):
        self.win = pygame.display.set_mode((1280, 720))

        self.scale = 1
        self.generate_points = lambda: self.generate_random_points(30, 100, 100, 500, 500)

        self.points = []
        self.line = []
        self.mesh = None

        self.generate_new()

        self.render_mesh = False

    def generate_new(self):
        self.points = self.generate_points()
        self.line = self.graham_scan(self.points)
        self.mesh = Triangulation(self.line).generate()

    def generate_random_points(self, amount, x, y, width, height):
        points = []
        for i in range(amount):
            px = random.random() * width + x
            py = random.random() * height + y
            points.append((int(px), int(py)))

        return points

    def draw(self):
        self.win.fill(0)

        for point in self.points:
            pygame.draw.rect(self.win, (255, 255, 255), ((point[0] * self.scale), (point[1] * self.scale), self.scale, self.scale))

        # for i, point in enumerate(self.line):
        #     p = (point[0] * self.scale, point[1] * self.scale)
        #     nxt =self.line[(i + 1) % len(self.line)]
        #     np = (nxt[0] * self.scale, nxt[1] * self.scale)
        #     pygame.draw.line(self.win, (255, 0, 0), p, np, self.scale)
        #     # pygame.draw.circle(self.win, (255, 0, 0), point, 3)

        # for p in self.line:
        #     pygame.draw.rect(self.win, (255, 255, 0), (p[0] * self.scale, p[1] * self.scale, self.scale, self.scale))

        if self.render_mesh:
            self.mesh.draw(self.win)

        pygame.display.update()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.generate_new()
                    if event.key == pygame.K_t:
                        self.render_mesh = not self.render_mesh


            self.draw()

    def get_lowest(self, points):
        lowest = (math.inf, math.inf)  # get lowest point

        for point in points:
            if point[1] == lowest[1]:
                lowest = min(point, lowest, key=lambda x: x[0])
                continue
            if point[1] < lowest[1]:
                lowest = point
        return lowest

    def sort_by_angle(self, lowest, p):
        x_diff = (p[0] - lowest[0])
        y_diff = (p[1] - lowest[1])

        if not x_diff and not y_diff:
            return -math.inf

        if not y_diff:
            y_diff = -1 / 100000

        return -math.atan2(x_diff, y_diff)

    def left_side(self, p1, p2, p3):
        x = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
        return x <= 0

    def graham_scan(self, points):
        stack = []

        lowest = self.get_lowest(points)

        points = sorted(points, key=lambda p: self.sort_by_angle(lowest, p))

        for point in points:
           #  self.draw()
            while len(stack) > 1 and self.left_side(stack[-2], stack[-1], point):
                # self.draw()
                stack.pop()

            stack.append(point)
        return stack


Main().loop()
