import pygame
import frac
import terminal as term

pygame.init()
disp = pygame.display.set_mode([700, 700])
pygame.display.set_caption("Game of Chaos")

fractal = frac.fractal(disp, 300, 300, 3, 250, 10000, (0, 0, 0))


# commands
def keys(args):
    file = open("keys.txt", "r")
    for i in file:
        print(i)

def set_radius(args):
    fractal.radius = int(args[0])
    fractal.reload()

def set_xy(args):
    fractal.x = int(args[0])
    fractal.y = int(args[1])
    fractal.reload()

def set_points(args):
    fractal.points = int(args[0])
    fractal.reload()

def set_fractal_points(args):
    fractal.fractal_points = int(args[0])

def set_color(args):
    c = []
    for i in range(0, 3):
        c.append(int(args[i]))
    fractal.color = c

def add_points(args):
    fractal.Xfractal.append(fractal.Xfrac)
    fractal.Yfractal.append(fractal.Yfrac)
    fractal.colors.append(fractal.colr)
    fractal.Xfrac = [fractal.Xfractal[-1][-1]]
    fractal.Yfrac = [fractal.Yfractal[-1][-1]]
    fractal.colr = [fractal.color]

def undo(args):
    del fractal.Xfractal[int(args[0])-1]
    del fractal.Yfractal[int(args[0])-1]

def lis(args):
    for i in range(0, len(fractal.Xfractal)):
        print(i+1)

def draw(args):
    if args[0] == "f":
        fractal.draw(True, True)
    elif args[0] == "o":
        fractal.draw(True, False)
    elif args[0] == "b":
        fractal.draw(False, True)
    else:
        fractal.draw(True, True)

def draw_points(args):
    if args[0] == "0":
        fractal.drawpoints = False
    elif args[0] == "1":
        fractal.drawpoints = True

def set_bg(args):
    c = []
    for i in range(0, 3):
        c.append(int(args[i]))
    fractal.bg_color = c

def gen_points(args):
    fractal.add_fractal_points()

def clear(args):
    fractal.Xfrac = [fractal.Xfractal[-1][-1]]
    fractal.Yfrac = [fractal.Yfractal[-1][-1]]
    fractal.colr = [fractal.color]

def reset(args):
    fractal.Xfractal = [[fractal.x]]
    fractal.Yfractal = [[fractal.y]]
    fractal.colors = [[fractal.color]]
    fractal.Xfrac = [fractal.Xfractal[-1][-1]]
    fractal.Yfrac = [fractal.Yfractal[-1][-1]]
    fractal.colr = [fractal.color]

def set_window_size(args):
    x = int(args[0])
    y = int(args[1])
    pygame.display.set_mode([x, y])


terminal = term.terminal("fractal-console")
terminal.add_command("add", term.add)
terminal.add_command("sub", term.sub)
terminal.add_command("keys", keys)
terminal.add_command("radius", set_radius)
terminal.add_command("setxy", set_xy)
terminal.add_command("points", set_points)
terminal.add_command("frpoints", set_fractal_points)
terminal.add_command("color", set_color)
terminal.add_command("addp", add_points)
terminal.add_command("undo", undo)
terminal.add_command("list", lis)
terminal.add_command("drawp", draw_points)
terminal.add_command("draw", draw)
terminal.add_command("bgcol", set_bg)
terminal.add_command("gen", gen_points)
terminal.add_command("clear", clear)
terminal.add_command("reset", reset)
terminal.add_command("winxy", set_window_size)


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                terminal.start_terminal()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                fractal.add_fractal_points()
                fractal.draw(True, True)
                #print("hello")

while True:
    event_handler()






