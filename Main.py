import pygame
import random


class Main:
    def __init__(self):
        self.win = pygame.display.set_mode((1280, 720))

        self.points = self.generate_random_points(10, 200, 200, 300, 400)

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
            pygame.draw.circle(self.win, (255, 255, 255), point, 3)

        pygame.display.update()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.draw()


Main().loop()
