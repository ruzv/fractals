import pygame

white = [255,255,255]


class dis:
    caption = "Setup"
    size = [1200, 800]
    backGround = white
    fps = 200

    def setSize(self, x, y):
        self.size = [x, y]
        pygame.display.set_mode(self.size)

    def setCaption(self, cap):
        self.caption = cap
        pygame.display.set_caption(self.caption)

    def setBackGround(self, col):
        self.backGround = col

    def setFps(self, num):
        self.fps = num

display = dis()