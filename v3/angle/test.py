import pygame
import math


pygame.init()
disp = pygame.display.set_mode([600, 600])



def draw(sc, x, y):
    pygame.draw.rect(sc, (0, 0, 0), [x, y, 20, 20])

def move(a, r, x, y):
    x += math.cos(math.radians(a)) * r
    y += math.sin(math.radians(a)) * r
    return x, y

x, y = 300, 300

def angle(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    if x == 0:
        return None
    a = math.degrees(math.atan(y/x))
    if x1 > x2:
        if y1 > y2:
            a += 180
        else:
            pass
    else:
        if y1 > y2:
            pass
        else:
            a += 0
    return (a)



ending = False
while ending != True:
    disp.fill((255, 255, 255))

    draw(disp, x, y)
    a = pygame.mouse.get_pos()
    print(a)
    #print(angle(x, y, a, b))

    pygame.display.update()
