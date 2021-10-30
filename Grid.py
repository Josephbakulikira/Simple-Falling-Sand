import pygame
import random

class Grid:
    def __init__(self, setting):
        self.rows = setting.rows + 1
        self.cols = setting.cols + 1
        self.cell_size = setting.cell_size
        self.screen = setting.window
        self.colors = setting.Colors
        #initialize Grid
        self.PreviousGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.CurrentGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.setting = setting
        self.currentType = 1

    def ResetGrid(self):
        self.PreviousGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.CurrentGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def UpdateGrid(self):
        for x in range(self.rows-1):
            for y in range(self.cols-1):
                if self.PreviousGrid[x][y] != self.setting.EMPTY:
                    self.UpdateSand(x, y)

    def UpdateSand(self, x, y):
        # check if the cell bellow is available
        if self.PreviousGrid[x][y+1] == self.setting.EMPTY:
            self.CurrentGrid[x][y] = self.setting.EMPTY
            self.CurrentGrid[x][y+1] = self.setting.SAND

        #check if the bottom left and bottom right right cells are available
        elif self.PreviousGrid[x-1][y+1] == 0 and self.PreviousGrid[x+1][y+1] == 0:
            #pick a random cell between the two
            choice = random.randint(0, 1)
            self.CurrentGrid[x][y] = 0

            if choice == 0:
                self.CurrentGrid[x - 1][y + 1] = 1
            else:
                self.CurrentGrid[x + 1][y + 1] = 1
        #check if the bottom right is available
        elif self.PreviousGrid[x+1][y+1] == self.setting.EMPTY:
            self.CurrentGrid[x][y] = self.setting.EMPTY
            self.CurrentGrid[x+1][y+1] = self.setting.SAND
        #check if the bottom left is available
        elif self.PreviousGrid[x-1][y+1] == 0:
            self.CurrentGrid[x][y] = 0
            self.CurrentGrid[x-1][y+1] = 1

    def Instantiate(self,x, y, value):
        self.CurrentGrid[x][y] = value

    def Draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                val = self.CurrentGrid[x][y]
                self.PreviousGrid[x][y] = val
                pygame.draw.rect(self.screen, self.colors[val], [int(x * self.cell_size), int((y - 1) * self.cell_size),
                self.cell_size-self.setting.offset,
                self.cell_size-self.setting.offset
                ])
