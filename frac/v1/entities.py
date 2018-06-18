import pygame
import drawing as dw
import math
import random

def end():
    pygame.quit()
    quit()

def getVel(p1x, p1y, p2x, p2y):
    x, y = 0, 0
    if p1x > p2x:
        x = p1x - p2x
    elif p1x < p2x:
        x = p2x - p1x

    if p1y > p2y:
        y = p1y - p2y
    elif p1y < p2y:
        y  = p2y - p1y

    v = math.sqrt(x*x + y*y)
    if v != 0:
        a = math.degrees(math.asin(x / v))
    else:
        a = 0

    if p1x > p2x:
        if p1y > p2y:
            a = 360 - a
        elif p1y < p2y:
            a = 180 + a
    elif p1x < p2x:
        if p1y > p2y:
            a = 0 + a
        elif p1y < p2y:
            a = 180 - a
    return a ,v

def dirVel(dir, vel, d = 2, m = 1):
    x = math.sin(math.radians(dir)) * ((vel/d)*m)
    y = -math.cos(math.radians(dir)) * ((vel/d)*m)
    return x, y

def circleAdd(num, a, it):
    for i in range(0 ,it):
        if a == num:
            a = 0
        else:
            a += 1
    return a

def figurePoints(points, vel, sx, sy):
    dir = 0
    n = 360 / points
    xx = []
    yy = []
    for i in range(0, points):
        x, y = dirVel(dir, vel, 1, 1)
        xx.append(sx+x)
        yy.append(sy+y)
        dir += n
    return xx, yy


rect = [[850, 50, 50, 850],[850, 850, 50, 50]]
penta = [[450,869,659,190,31],[50,355,850,850,355]]
tri = [[450,50,850],[50,742,742]]
smTri = [[450,400,500],[406,493,493]]
smPenta = [[450,509,486,414,391],[400,443,500,500,443]]
hex = [[250, 650, 850, 650, 250, 50], [50, 50, 396, 743, 743, 396]]

class frac:

    div = 2
    mul = 1

    pointsX = []
    pointsY = []
    col = []

    x, y = figurePoints(6, 400, 450, 450)
    print(x, y)

    px = 0
    py = 0

    last = 0



    def update(self):
        i = random.randint(0,4)
        while i == self.last:
            i = random.randint(0, 4)

        #while i == circleAdd(4, self.last, 1) or i == circleAdd(4, self.last, 3):
         #   i = random.randint(0, 4)

        self.last = i

        a, v = getVel(self.px, self.py, self.x[i], self.y[i])
        x, y = dirVel(a, v, self.div, self.mul)

        self.px += x
        self.py += y

        self.pointsX.append(self.px)
        self.pointsY.append(self.py)

    def reSet(self):
        self.pointsX = []
        self.pointsY = []

    def color(self):
        a = random.randint(0,2)
        if a == 0:
            return "r"
        elif a == 1:
            return "g"
        elif a == 2:
            return "b"

    def draw(self, sc):
        for i in range(0, len(self.pointsX)):
            #print(self.pointsX[i], self.pointsY[i])
            #if self.pointsX[i] > 0 and self.pointsY[i] > 0 and self.pointsX[i] < 4000000 and self.pointsY[i] < 4000000:
            pygame.draw.rect(sc, (0, 0, 0), [self.pointsX[i], self.pointsY[i], 1, 1])


    def adraw(self, sc):
        for i in range(0, len(self.pointsX)):
            #print(self.pointsX[i], self.pointsY[i])
            #if self.pointsX[i] > 0 and self.pointsY[i] > 0 and self.pointsX[i] < 4000000 and self.pointsY[i] < 4000000:
            if self.color() == "r":
                pygame.draw.rect(sc, (255, 0, 0), [self.pointsX[i], self.pointsY[i], 1,1])
            elif self.color() == "g":
                pygame.draw.rect(sc, (0, 255, 0), [self.pointsX[i], self.pointsY[i], 1,1])
            elif self.color() == "b":
                pygame.draw.rect(sc, (0, 0, 255), [self.pointsX[i], self.pointsY[i], 1,1])

