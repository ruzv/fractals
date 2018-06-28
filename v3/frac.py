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
    drawpoints = False
    bg_color = [255, 255, 255]

    Xfractal = []
    Yfractal = []
    Xfrac = []
    Yfrac = []
    colors = []
    colr = []
    fractal_points = 0

    color = []
    Xpoints = []
    Ypoints = []
    points = 0
    x, y = 0, 0

    def __init__(self, sc, x, y, p, r, fr_p, c):
        self.surface = sc
        self.x = x
        self.y = y
        self.points = p
        self.radius = r
        self.fractal_points = fr_p
        self.color = c
        self.Xpoints, self.Ypoints = generate_points(x, y, p, r)

        self.Xfrac.append(x)
        self.Yfrac.append(y)
        self.colr.append(self.color)

    #redo
    def reload(self):
        self.Xpoints, self.Ypoints = generate_points(self.x, self.y, self.points, self.radius)

    def get_fractal_point(self):
        p = random.randint(0, self.points-1)
        a = get_angle(self.Xfrac[-1], self.Yfrac[-1], self.Xpoints[p], self.Ypoints[p])
        while a == None:
            p = random.randint(0, self.points-1)
            a = get_angle(self.Xfrac[-1], self.Yfrac[-1], self.Xpoints[p], self.Ypoints[p])

        d = get_distance(self.Xfrac[-1], self.Yfrac[-1], self.Xpoints[p], self.Ypoints[p])
        d = d/2

        x = math.cos(math.radians(a))*d
        y = math.sin(math.radians(a))*d

        self.Xfrac.append(self.Xfrac[-1]+x)
        self.Yfrac.append(self.Yfrac[-1]+y)
        self.colr.append(self.color)

    def add_fractal_points(self):
        for i in range(0, self.fractal_points):
            self.get_fractal_point()
        #print(len(self.Xfractal), len(self.Yfractal))

    def draw_fractal(self):
        for s in range(0, len(self.Xfractal)):
            for i in range(0, len(self.Xfractal[s])):
                pygame.draw.rect(self.surface, self.colors[s][i], [self.Xfractal[s][i], self.Yfractal[s][i], 1, 1])

    def draw_frac(self):
        for i in range(0, len(self.Xfrac)):
            pygame.draw.rect(self.surface, self.colr[i], [self.Xfrac[i], self.Yfrac[i], 1, 1])
    
    def draw_points(self):
        for i in range(0, len(self.Xpoints)):
            pygame.draw.circle(self.surface, (0, 0, 0), [self.Xpoints[i], self.Ypoints[i]], 3)

    def draw(self, fracta, frac):
        self.surface.fill(self.bg_color)
        if fracta == True:
            self.draw_fractal()
        if frac == True:
            self.draw_frac()
        #print(self.drawpoints)
        if self.drawpoints == True:
            self.draw_points()
        pygame.display.update()

