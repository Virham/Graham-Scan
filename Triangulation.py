import pygame
import random


class Triangulation:
    def __init__(self, convex_hull):
        self.convex_hull = convex_hull

    def generate(self):
        indices = []

        for i in range(len(self.convex_hull) - 2):
            indices.append(0)
            indices.append(i+1)
            indices.append(i+2)

        return Mesh(self.convex_hull, indices)


class Mesh:
    def __init__(self, vertices, indices):
        self.vertices = vertices
        self.indices = indices
        self.color = self.generate_colors()

    def generate_colors(self):
        colors = []
        i = 0

        while i < len(self.indices):
            color = (random.random() * 255, random.random() * 255, random.random() * 255)
            colors.append(color)

            i += 3

        return colors

    def draw(self, win):
        i = 0
        while i < len(self.indices):
            v1 = self.indices[i]
            v2 = self.indices[i+1]
            v3 = self.indices[i+2]

            pygame.draw.polygon(win, self.color[i // 3], [self.vertices[v1], self.vertices[v2], self.vertices[v3]])
            i += 3

        for vertex in self.vertices:
            pygame.draw.circle(win, (255, 0, 0), vertex, 3)
