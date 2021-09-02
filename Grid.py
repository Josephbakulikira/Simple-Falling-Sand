import pygame
import random

class Grid:
    def __init__(self, rows, cols, cell_size):
        self.rows = rows + 1
        self.cols = cols + 1
        self.cell_size = cell_size
        #initialize Grid
        self.PreviousGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.CurrentGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def ResetGrid(self):
        self.PreviousGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.CurrentGrid = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def UpdateGrid(self):
        for x in range(self.rows-1):
            for y in range(self.cols-1):
                if self.PreviousGrid[x][y] != 0:
                    # check if the cell below is available
                    if self.PreviousGrid[x][y + 1] == 0:
                        self.CurrentGrid[x][y] = 0
                        self.CurrentGrid[x][y+1] = 1
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
                    elif self.PreviousGrid[x+1][y+1] == 0:
                        self.CurrentGrid[x][y] = 0
                        self.CurrentGrid[x+1][y+1] = 1
                    #check if the bottom left is available
                    elif self.PreviousGrid[x-1][y+1] == 0:
                        self.CurrentGrid[x][y] = 0
                        self.CurrentGrid[x-1][y+1] = 1

    def Instantiate(self,x, y, value):
        self.CurrentGrid[x][y] = value

    def Draw(self, screen):
        for x in range(self.rows):
            for y in range(self.cols):
                self.PreviousGrid[x][y] = self.CurrentGrid[x][y]
                if self.CurrentGrid[x][y] != 0:
                    pygame.draw.rect(screen, (255, 255, 0), [int(x * self.cell_size), int((y - 1) * self.cell_size), self.cell_size, self.cell_size])
