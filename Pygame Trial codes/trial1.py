import pygame, sys
from pygame.locals import *

pygame.init() #This Needs to be called before any pygame program

fpsClock = pygame.time.Clock() #The Clock object makes sure our app runs at certain FPS
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Trial Program No.1')
whiteColor = (255, 255, 255)
############################################################

pictureObj = pygame.image.load('Picture.jpg')

while True: # This loop is main app loop
    screen.fill(whiteColor) # BackGround Color
    screen.blit(pictureObj,(60,50))

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(30)
     


