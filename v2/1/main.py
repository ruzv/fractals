import pygame
import math
import entities as en

pygame.init()
dis = pygame.display.set_mode([800, 800])
pygame.display.set_caption("fractals")

frac = en.fractal(dis, 400, 400, 3, 350)

for i in range(1000000):
    frac.get_frac_point()
#print(frac.border_points)

def end():
    pygame.quit()
    quit()

def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()

def drawLoop():
    dis.fill((255, 255, 255))
    #frac.draw_border_points()
    frac.draw_points()

def gameLoop():
    eventHandler()

while True:
    gameLoop()
    drawLoop()
    pygame.display.update()


eventHandler()