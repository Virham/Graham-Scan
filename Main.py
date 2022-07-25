# https://en.wikipedia.org/wiki/Graham_scan

import pygame
import random
import math
import time


class Main:
    def __init__(self):
        self.win = pygame.display.set_mode((1280, 720))

        self.points = self.generate_random_points(25, 200, 200, 500, 500)
        self.line = self.graham_scan(self.points)

    def generate_random_points(self, amount, x, y, width, height):
        points = []
        for i in range(amount):
            px = random.random() * width + x
            py = random.random() * height + y
            points.append((px, py))
        return points

    def draw(self):
        self.win.fill(0)

        for point in self.points:
            pygame.draw.rect(self.win, (255, 255, 255), (int(point[0]), int(point[1]), 1, 1))

        for i, point in enumerate(self.line):
            pygame.draw.line(self.win, (255, 0, 0), point, self.line[(i + 1) % len(self.line)])
            pygame.draw.rect(self.win, (255, 255, 0), (point[0], point[1], 1, 1))
            # pygame.draw.circle(self.win, (255, 0, 0), point, 3)


        pygame.display.update()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.draw()

    def get_lowest(self, points):
        lowest = (math.inf, math.inf)  # get lowest point

        for point in points:
            if point[1] == lowest[1]:
                print(point, lowest)
                lowest = min(point, lowest, key=lambda x: x[0])
                continue
            if point[1] < lowest[1]:
                lowest = point
        print(lowest)
        return lowest

    def sort_by_angle(self, lowest, p):
        x_diff = (p[0] - lowest[0])
        y_diff = (p[1] - lowest[1])

        return -math.atan2(x_diff, y_diff) if lowest != p else -math.inf

    def left_side(self, p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) <= 0

    def graham_scan(self, points):
        stack = []

        lowest = self.get_lowest(points)
        points = sorted(points, key=lambda p: self.sort_by_angle(lowest, p))
        print(points)
        for point in points:
            while len(stack) > 1 and self.left_side(stack[-2], stack[-1], point):
                stack.pop()

            stack.append(point)

        return stack


Main().loop()
