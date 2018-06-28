import pygame
import fractal as frc
import terminal as trm

pygame.init()
disp = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Fractal")

fractal = frc.frac(disp, 200, 200, 150, (0, 0, 0), 6)

terminal = trm.terminal("fractal")


while True:
    fractal.generate_batch()
    disp.fill((255, 255, 255))
    fractal.draw_batch()
    pygame.display.update()

