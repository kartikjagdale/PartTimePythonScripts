import threading,random,sys,pygame

#Constants
NUM_WORMS = 5
FPS =15
CELL_SIZE = 20
CELLS_WIDE = 32
CELLS_HIGH =24

GRID = []
for x in range(CELLS_WIDE):
    GRID.append([None]*CELLS_HIGH)

GRID_LOCK = threading.Lock()
WORMS_RUNNING = True
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

HEAD = 0
BUTT = -1

class Worm(threading.Thread):
    def __init__(self,name='Worm',maxsize=None,color=None,speed=None):
        threading.Thread.__init__(self)
        self.name=name
        
