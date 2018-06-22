import pygame
import random
import math


def generate_points(x, y, p, r):
    a = 0
    lx, ly = [], []
    for i in range(p):
        px = math.cos(math.radians(a)) * r
        py = math.sin(math.radians(a)) * r
        lx.append(int(round(x+px, 0)))
        ly.append(int(round(y+py, 0)))
        a += 360 / p
    return lx, ly

def get_distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return math.sqrt(x**2+y**2)

def get_angle(x1, y1, x2, y2):
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

class fractal:

    surface = None

    Xfractal = []
    Yfractal = []
    fractal_points = 0

    Xpoints = []
    Ypoints = []
    points = 0
    x, y = 0, 0

    def __init__(self, sc, x, y, p, r, fr_p):
        self.surface = sc
        self.x = x
        self.y = y
        self.points = p
        self.radius = r
        self.Xfractal.append(x)
        self.Yfractal.append(y)
        self.fractal_points = fr_p
        self.Xpoints, self.Ypoints = generate_points(x, y, p, r)

    def get_fractal_point(self, x, y):
        p = random.randint(0, self.points-1)
        a = get_angle(x, y, self.Xpoints[p], self.Ypoints[p])
        while a == None:
            p = random.randint(0, self.points-1)
            a = get_angle(x, y, self.Xpoints[p], self.Ypoints[p])

        d = get_distance(x, y, self.Xpoints[p], self.Ypoints[p])
        d = d/2

        X = math.cos(math.radians(a))*d
        Y = math.sin(math.radians(a))*d

        return x+X, y+Y

    def add_fractal_points(self):
        i = 0
        x = self.Xfractal[-1]
        y = self.Yfractal[-1]
        while i < self.fractal_points:
            x, y = self.get_fractal_point(x, y)
            x = int(round(x, 0))
            y = int(round(y, 0))
            print(x, y)
            if not(x in self.Xfractal) and not(y in self.Yfractal):
                self.Xfractal.append(x)
                self.Yfractal.append(y)
                i += 1

    def draw_fractal(self):
        for i in range(1, len(self.Xfractal)):
            pygame.draw.rect(self.surface, (0, 0, 0), [self.Xfractal[i], self.Yfractal[i], 1, 1])
    
    def draw_points(self):
        for i in range(0, len(self.Xpoints)):
            pygame.draw.circle(self.surface, (0, 0, 0), [self.Xpoints[i], self.Ypoints[i]], 3)

    def draw(self):
        self.surface.fill((255, 255, 255))
        self.draw_fractal()
        self.draw_points()
        pygame.display.update()
