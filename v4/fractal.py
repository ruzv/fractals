import pygame
import random
import math


# point functions
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

class frac:

    # pygame.display for drawing the fractal
    surface = None

    # position of the center of the fractal. for regular fractal (generate_figure_points)
    center_x = 0
    center_y = 0

    radius = 0
    color = [0, 0, 0]
    
    # the amounth of end points of the fractal
    figure_points = 0
    # end points of the fractal
    figure_points_x = []
    figure_points_y = []

    # lists of batches of points and batches of color.
    fractal_points_x = []
    fractal_points_y = []
    fractal_color = []

    # batch of points and color
    batch_points_x = []
    batch_points_y = []
    batch_color = []
    batch_size = 100000


    def __init__(self, s, x, y, r, c, p):
        self.surface = s
        self.center_x = x
        self.center_y = y
        self.radius = r
        self.color = c
        self.figure_points = p
        
        self.batch_points_x = [x]
        self.batch_points_y = [y]
        self.batch_color = [self.color]
        self.fractal_points_x = [self.batch_points_x]
        self.fractal_points_y = [self.batch_points_y]
        self.fractal_color = [self.batch_color]
        self.generate_figure_points()
    
    # generates the end points of the fractal
    def generate_figure_points(self):
        a = 0
        self.figure_points_x, self.figure_points_y = [], []
        for i in range(self.figure_points):
            px = math.cos(math.radians(a)) * self.radius
            py = math.sin(math.radians(a)) * self.radius
            self.figure_points_x.append(self.center_x+px)# round(int(x), 0)
            self.figure_points_y.append(self.center_y+py)# round(int(y), 0)
            a += 360 / self.figure_points

    # returns one point of the fractal
    def get_fractal_point(self):
        p = random.randint(0, self.figure_points-1)
        a = get_angle(self.batch_points_x[-1], self.batch_points_y[-1], self.figure_points_x[p], self.figure_points_y[p])
        while a == None:
            p = random.randint(0, self.figure_points-1)
            a = get_angle(self.batch_points_x[-1], self.batch_points_y[-1], self.figure_points_x[p], self.figure_points_y[p])

        d = get_distance(self.batch_points_x[-1], self.batch_points_y[-1], self.figure_points_x[p], self.figure_points_y[p])

        d = d / 2

        x = math.cos(math.radians(a)) * d
        y = math.sin(math.radians(a)) * d
            
        return self.batch_points_x[-1]+x, self.batch_points_y[-1]+y

    # generates a batch of fractal points. 
    def generate_batch(self):
        for n in range(0, self.batch_size):
            x, y = self.get_fractal_point()
            self.batch_points_x.append(x)
            self.batch_points_y.append(y)
            self.batch_color.append(self.color)

    def draw_batch(self):
        for p in range(1, len(self.batch_points_x)):
            pygame.draw.rect(self.surface, self.batch_color[p], [self.batch_points_x[p], self.batch_points_y[p], 1, 1])


# fr = frac(0, 0, 20, (0, 0, 0), 3)
# fr.generate_figure_points()
# fr.generate_batch()
# print(fr.batch_points_x)
# print(fr.batch_points_y)

# print(fr.figure_points_x)
# print(fr.figure_points_y)
