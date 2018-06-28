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

def read(file):
    file = open(file, "r")
    for i in file:
        print(i)


class fractal:


    def __init__(self, sc, x, y, p, r, fr_p):
        self.surface = sc
        self.x = x
        self.y = y
        self.points = p
        self.radius = r
        self.x_fractal, self.y_fractal = [x], [y]
        self.x_points, self.y_points = generate_points(x, y, p, r)
        self.fractal_points = fr_p
        self.top = 1
        self.bot = 2

    def get_frac_points(self):
        for i in range(self.fractal_points):
            n = random.randint(0, self.points-1)
            a = get_angle(self.x_fractal[-1], self.y_fractal[-1], self.x_points[n], self.y_points[n])
            while a == None:
                n = random.randint(0, self.points-1)
                a = get_angle(self.x_fractal[-1], self.y_fractal[-1], self.x_points[n], self.y_points[n])
            d = get_distance(self.x_fractal[-1], self.y_fractal[-1], self.x_points[n], self.y_points[n])
            d = self.top*d / self.bot
            x = math.cos(math.radians(a)) * d
            y = math.sin(math.radians(a)) * d
            self.x_fractal.append(self.x_fractal[-1]+x)
            self.y_fractal.append(self.y_fractal[-1]+y)

    def reset(self):
        self.x_fractal = [self.x]
        self.y_fractal = [self.y]

    def save(self):
        name = str(self.points)+"-"+str(self.top)+"-"+str(self.bot)+".txt"
        file = open(name, "w")
        for i in range(0, len(self.x_fractal)):
            file.write(str(self.x_fractal[i])+" "+str(self.y_fractal[i])+" \n")
        file.close

    def terminal(self, command):
        command = command.split(" ")
        for q in range(1):
            if command[0] == "help":
                read("help.txt")
            elif command[0] == "exit":
                break
            elif command[0] == "quit":
                pygame.quit()
                quit()
            elif command[0] == "points":
                try:
                    self.points = int(command[1])
                    self.x_points, self.y_points = generate_points(self.x, self.y, self.points, self.radius)
                except:
                    print("invalid command")
            elif command[0] == "reset":
                self.reset()
            elif command[0] == "fractal-points":
                try:
                    self.fractal_points = int(command[1])
                except:
                    print("invalid command")
            elif command[0] == "radius":
                try:
                    self.radius = int(command[1])
                except:
                    print("invalid command")
            elif command[0] == "pos":
                try:
                    self.x = int(command[1])
                    self.y = int(command[2])
                except:
                    print("invalis command")
            elif command[0] == "window-size":
                try:
                    x = int(command[1])
                    y = int(command[2])
                    pygame.display.set_mode((x, y))
                except:
                    print("invalid command")
            elif command[0] == "top":
                try:
                    self.top = int(command[1])
                except:
                    print("invalid command")
            elif command[0] == "bot":
                try:
                    self.bot = int(command[1])
                except:
                    print("invalid command")
            elif command[0] == "save":
                self.save()
            else:
                print(command, "is not understood. Try help for help.")

            command = input("terminal: ")
            self.terminal(command)

    def draw_fractal(self):
        for i in range(1, len(self.x_fractal)):
            #print(self.x_fractal[i], self.y_fractal[i])
            pygame.draw.rect(self.surface, (0, 0, 0), [self.x_fractal[i], self.y_fractal[i], 1, 1])

    def draw_points(self):
        for i in range(0, self.points):
            pygame.draw.circle(self.surface, (0, 0, 0), [self.x_points[i], self.y_points[i]], 2)

    def draw(self):
        self.draw_fractal()
        self.draw_points()