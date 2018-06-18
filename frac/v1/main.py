import pygame
import drawing as dw
import entities as en

pygame.init()
dis = pygame.display.set_mode([20,20])
dw.display.setSize(900, 900)
dw.display.setCaption("Setup")
clock = pygame.time.Clock()

def end():
    pygame.quit()
    quit()

def eventHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(0, 100000):
                    fc.update()
            if event.key == pygame.K_z:
                for i in range(0, 1000000):
                    try:
                        fc.update()
                    except:
                        print("s", end = "")
            if event.key == pygame.K_r:
                fc.reSet()

            if event.key == pygame.K_EQUALS:
                fc.div += 1
                print("div", fc.div)
            if event.key == pygame.K_MINUS:
                fc.div -= 1
                print("div", fc.div)
            if event.key == pygame.K_9:
                fc.mul -= 1
                print("mul", fc.mul)
            if event.key == pygame.K_0:
                fc.mul += 1
                print("mul", fc.mul)

def drawLoop():
    dis.fill(dw.display.backGround)
    fc.draw(dis)

def gameLoop():
    eventHandler()
    #fc.update()

fc = en.frac()

endGame = False
while not endGame:
    gameLoop()
    drawLoop()
    clock.tick(dw.display.fps)
    pygame.display.update()
end()
