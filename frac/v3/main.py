import pygame
import frac

pygame.init()
disp = pygame.display.set_mode([950, 950])
pygame.display.set_caption("Game of Chaos")

fractal = frac.fractal(disp, 50, 50, 3, 300, 200)
fractal.get_frac_points()
print(fractal.x_fractal)

def draw():

    pygame.display.update()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    






