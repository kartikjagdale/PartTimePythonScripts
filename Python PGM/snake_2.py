#Simple Snake Game
#Author: Hebi
#Reference: InventWithPython.com
import pygame, sys, random, time
from pygame.locals import *
FPS = 10
""" Constant Vaiables """
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

""" Constant Values for Different Colors """
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)

BGCOLOR = BLACK

"""Contant Values for each directions"""
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
""" Main Function """
def main():
    global fpsClock, winobj, BASICFONT
    pygame.init()
    fpsClock = pygame.time.Clock()
    BASICFONT = pygame.font.Font('freesansbold.ttf',18)
    winobj = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Simple Snake Game')
    showStartScreen()
    while True: #Main application Loop
        gameloop()
        showGameOverScreen()

        #End of the Main Application Loop
""" END of Main Function """

""" Start screen Function """
def showStartScreen():#Animation Part of Start Screen
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Snake!', True, GREEN)
    pressKeySurf = BASICFONT.render('Press a key to START', True, DARKGRAY)

    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH -200, WINDOWHEIGHT -30)

    degrees1 = 0
    degrees2 =0
    while True:
        winobj.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1,degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    
        winobj.blit(rotatedSurf1, rotatedRect1)
    
        rotatedSurf2 = pygame.transform.rotate(titleSurf2,degrees2)
        rotatedRect2 = rotatedSurf1.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    
        winobj.blit(rotatedSurf2, rotatedRect2)
        winobj.blit(pressKeySurf, pressKeyRect) #Animation Part Over

        if checkforKeyPress():
            return
        pygame.display.update()
        fpsClock.tick(FPS)

        degrees1 += 3
        degrees2 += 7
        if degrees1 > 360:
            degrees1 -= 360
        if degrees2 > 360:
            degrees2 -= 360

"""Main Game Loop Function """
def gameloop():
    startx = random.randint(5,CELLWIDTH - 6)
    starty = random.randint(5,CELLHEIGHT - 6)
    snakeCoords = [(startx,starty),(startx-1,starty-1)]
    direction = RIGHT

    apple = (random.randint(0,CELLWIDTH -1),random.randint(0,CELLHEIGHT-1))
    apple1 = (random.randint(0,CELLWIDTH -1),random.randint(0,CELLHEIGHT-1))

    while True:
        #Get Player Input
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                if event.key == K_ESCAPE:
                    terminate()
        #Check if snake has Hit Itself
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
            return
        for snakeBody in snakeCoords[1:]: 
            if (snakeCoords[0][0],snakeCoords[0][1]) == snakeBody:
                return
        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))

        elif snakeCoords[0][0] == apple1[0] and snakeCoords[0][1] == apple1[1]:
             apple1 = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
        else:
            snakeCoords.pop() #makes the last segment of snake disappear

        if direction == UP:
            snakeCoords.insert(0, (snakeCoords[0][0],snakeCoords[0][1]-1))
        elif direction == DOWN:
            snakeCoords.insert(0,(snakeCoords[0][0], snakeCoords[0][1]+1))
        elif direction == LEFT:
            snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        elif direction == RIGHT:
            snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))
        winobj.fill(BGCOLOR)
        drawGrid()
        drawSnake(snakeCoords)
        drawApple(apple)
        drawApple(apple1)
        drawScore(len(snakeCoords))
        pygame.display.update()
        fpsClock.tick(FPS)
""" Game over screen function """
def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    winobj.blit(gameSurf, gameRect)
    winobj.blit(overSurf, overRect)
    pygame.display.update()
    time.sleep(0.5)
    while True:
        if checkforKeyPress():
            return




"""Check for Key Press"""
def checkforKeyPress():
    for event in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        return event.key

def terminate():
    pygame.quit()
    sys.exit()

""" Draw Snake Function"""
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        coordRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(winobj, GREEN, coordRect)

""" Draw Apple Function"""
def drawApple(apple):
    x = apple[0] * CELLSIZE
    y = apple[1] * CELLSIZE
    appleRect = pygame.Rect(x,y,CELLSIZE,CELLSIZE)
    pygame.draw.rect(winobj, RED, appleRect)

"""Draw Score Function"""
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH-80, 10)
    winobj.blit(scoreSurf, scoreRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(winobj, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(winobj, DARKGRAY, (0, y), (WINDOWWIDTH, y))



if __name__ == '__main__':
    main()





















