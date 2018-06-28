import pygame
import frac

pygame.init()
disp = pygame.display.set_mode([950, 950])
pygame.display.set_caption("Game of Chaos")


fractal = frac.fractal(disp, 475, 475, 3, 450, 20000)

print("press ENTER for terminal")

def draw():
    disp.fill((255, 255, 255))
    fractal.draw()
    pygame.display.update()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                draw()
            if event.key == pygame.K_RETURN:
                command = input("terminal: ")
                fractal.terminal(command)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                fractal.get_frac_points()
                draw()
            if event.key == pygame.K_c:
                fractal.reset()
                draw()
            if event.key == pygame.K_2:
                fractal.top += 1
                print(fractal.top, "/", fractal.bot)
            if event.key == pygame.K_1:
                if fractal.top != 1:
                    fractal.top -= 1
                print(fractal.top, "/", fractal.bot)
            if event.key == pygame.K_w:
                fractal.bot += 1
                print(fractal.top, "/", fractal.bot)
            if event.key == pygame.K_q:
                if fractal.bot != 1:
                    fractal.bot -= 1
                print(fractal.top, "/", fractal.bot)


while True:
    event_handler()






