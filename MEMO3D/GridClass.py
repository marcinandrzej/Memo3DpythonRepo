import random

from OpenGL.GL import *

from FieldClass import FieldClass

class GridClass():

    def __init__(self, offset):

        self.firstClick = True
        self.hit = False
        self.firstLocation = [0, 0]
        self.secondLocation = [0, 0]

        self.offset = offset

        self.player_pointer = [0, 0]

        self.grid = []
        for rows in range(4):
            self.grid.append([])
            for cols in range(4):
                self.grid[rows].append(2*rows + cols//2)

        self.shuffle()

        self.game = []
        for rows in range(4):
            self.game.append([])
            for cols in range(4):
                color_ind = self.grid[rows][cols]
                self.game[rows].append(FieldClass(rows, cols, color_ind, self.offset))

        for x in range(4):
            for y in range(4):
                self.grid[x][y] = 0

        self.game[0][0].setPointer()

    def shuffle(self):

        randi = random.randrange(30, 40)
        for i in range(randi):
            randx1 = random.randrange(4)
            randy1 = random.randrange(4)
            randx2 = random.randrange(4)
            randy2 = random.randrange(4)

            temp = self.grid[randx1][randy1]
            self.grid[randx1][randy1] = self.grid[randx2][randy2]
            self.grid[randx2][randy2] = temp

    def checkWin(self):
        if (self.grid[0][0] == self.grid[0][1] == self.grid[0][2] == self.grid[0][3] ==
                self.grid[1][0] == self.grid[1][1] == self.grid[1][2] == self.grid[1][3] ==
                self.grid[2][0] == self.grid[2][1] == self.grid[2][2] == self.grid[2][3] ==
                self.grid[3][0] == self.grid[3][1] == self.grid[3][2] == self.grid[3][3] == 1):
            return True
        else:
            return False

    def moveUp(self):
        if self.player_pointer[0] > 0:
            self.game[self.player_pointer[0]][self.player_pointer[1]].unsetPointer()
            self.player_pointer[0] -= 1
            self.game[self.player_pointer[0]][self.player_pointer[1]].setPointer()

    def moveDown(self):
        if self.player_pointer[0] < 3:
            self.game[self.player_pointer[0]][self.player_pointer[1]].unsetPointer()
            self.player_pointer[0] += 1
            self.game[self.player_pointer[0]][self.player_pointer[1]].setPointer()

    def moveRight(self):
        if self.player_pointer[1] < 3:
            self.game[self.player_pointer[0]][self.player_pointer[1]].unsetPointer()
            self.player_pointer[1] += 1
            self.game[self.player_pointer[0]][self.player_pointer[1]].setPointer()

    def moveLeft(self):
        if self.player_pointer[1] > 0:
            self.game[self.player_pointer[0]][self.player_pointer[1]].unsetPointer()
            self.player_pointer[1] -= 1
            self.game[self.player_pointer[0]][self.player_pointer[1]].setPointer()

    def draw(self):

        glPushMatrix()
        for row in range(4):
            for col in range(4):
                self.game[row][col].draw()
        glPopMatrix()

    def update(self):
            row = self.player_pointer[0]
            col = self.player_pointer[1]
            if self.firstClick:
                if self.grid[row][col] == 0:
                    if not self.hit:
                        self.grid[self.firstLocation[0]][self.firstLocation[1]] = 0
                        self.game[self.firstLocation[0]][self.firstLocation[1]].rotate()
                        self.grid[self.secondLocation[0]][self.secondLocation[1]] = 0
                        self.game[self.secondLocation[0]][self.secondLocation[1]].rotate()
                    self.hit = False
                    self.firstLocation = [row, col]
                    self.grid[row][col] = 1
                    self.game[row][col].rotate()
                    self.firstClick = False
            else:
                if self.grid[row][col] == 0:
                    self.secondLocation = [row, col]
                    self.grid[row][col] = 1
                    self.game[row][col].rotate()
                    if (self.game[self.firstLocation[0]][self.firstLocation[1]].getColorIndex()
                            == self.game[self.secondLocation[0]][self.secondLocation[1]].getColorIndex()):
                        self.hit = True
                    self.firstClick = True