import pygame
import frac
import terminal as term

pygame.init()
disp = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Game of Chaos")

fractal = frac.fractal(disp, 150, 150, 3, 100, 10)


def keys(args):
    file = open("keys.txt", "r")
    for i in file:
        print(i)



terminal = term.terminal("fractal-console")
terminal.add_command("add", term.add)
terminal.add_command("sub", term.sub)
terminal.add_command("keys", keys)



def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                terminal.terminal()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                fractal.add_fractal_points()
                fractal.draw()
                print("hello")


while True:
    event_handler()






