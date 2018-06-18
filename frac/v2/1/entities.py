import pygame
import random
import math

def end():
    pygame.quit()
    quit()




"""
        x = self.chaser_speed * math.cos(math.radians(angle))
        y = self.chaser_speed * math.sin(math.radians(angle))
"""


class fractal:

    border_points = [[0], [0]]
    fractal_points = [[0], [0]]

    def __init__(self, sc, x, y, points, radius):
        self.surface = sc
        self.points = points
        self.fractal_points = [[x], [y]]
        self.border_points = self.get_br_points(x, y, points, radius)

    def get_distance(self, x1, y1, x2, y2):
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        return math.sqrt(x**2+y**2)

    def angle(self, x1, y1, x2, y2):
        x = abs(x1 - x2)
        y = abs(y1 - y2)
        if x == 0:
            return None
        a = math.degrees(math.atan(y/x))
        if x1 > x2:
            if y1 > y2:
                a += 180
            else:
                a = (90 - a) + 90
        else:
            if y1 > y2:
                a  = (90 - a) + 270
            else:
                a += 0
        return a

    def get_br_points(self, center_x, center_y, p, r):
        a = -90
        xx = []
        yy = []
        for i in range(p):
            y = math.sin(math.radians(a)) * r
            x = math.cos(math.radians(a)) * r
            xx.append(int(round(center_x+x, 0)))
            yy.append(int(round(center_y+y, 0)))
            a += 360 / p
        return [xx, yy]

    def get_frac_point(self):
        n = random.randint(0, self.points-1)
        a = self.angle(self.fractal_points[0][-1], self.fractal_points[1][-1], self.border_points[0][n], self.border_points[1][n])
        while a == None:
            n = random.randint(0, self.points-1)
            a = self.angle(self.fractal_points[0][-1], self.fractal_points[1][-1], self.border_points[0][n], self.border_points[1][n])

        d = self.get_distance(self.fractal_points[0][-1], self.fractal_points[1][-1],self.border_points[0][n], self.border_points[1][n])

        d = d*3 / 5

        x = int(round(math.cos(math.radians(a)) * d, 0))
        y = int(round(math.sin(math.radians(a)) * d, 0))

        self.fractal_points[0].append(self.fractal_points[0][-1]+x)
        self.fractal_points[1].append(self.fractal_points[1][-1]+y)


    def draw_border_points(self):
        for i in range(0, len(self.border_points[0])):
            pygame.draw.circle(self.surface, (0, 0, 0), [self.border_points[0][i], self.border_points[1][i]], 3)

    def draw_points(self):
        for i in range(1, len(self.fractal_points[0])):
            print((self.fractal_points[0][i], self.fractal_points[1][i]))
            pygame.draw.rect(self.surface, (0, 0, 0), (self.fractal_points[0][i], self.fractal_points[1][i], 1, 1))
            #pygame.draw.circle(self.surface, (0, 0, 0), (self.fractal_points[0][i], self.fractal_points[1][i]), 1)