import pygame

class fractal:


    def __init__(self, sc, name):
        self.surface = sc
        self.x_fractal = []
        self.y_fractal = []
        self.get_fractal(open(name, "r"))
        print(self.x_fractal)
        print(self.y_fractal)

    def get_fractal(self, file):
        for i in file:
            a = i.split(" ")
            self.x_fractal.append(float(a[0]))
            self.y_fractal.append(float(a[1]))

    def draw_fractal(self):
        for i in range(1, len(self.x_fractal)):
            #print(self.x_fractal[i], self.y_fractal[i])
            pygame.draw.rect(self.surface, (0, 0, 0), [self.x_fractal[i], self.y_fractal[i], 1, 1])

    def draw(self):
        self.draw_fractal()

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


pygame.init()
disp = pygame.display.set_mode((950, 950))

name = "6-2-3.txt"
frac = fractal(disp, name)


disp.fill((255, 255, 255))
frac.draw()
pygame.display.update()
while True:
    event_handler()