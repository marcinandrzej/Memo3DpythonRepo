import pygame
from pygame.locals import *


from OpenGL.GL import *
from OpenGL.GLU import *

from GridClass import GridClass

class GameClass():

    def __init__(self, window_w, window_h):

        pygame.init()
        self.display = (window_w, window_h)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("MEMO3D")
        glEnable(GL_DEPTH_TEST)

        self.win = False

        self.game = GridClass(2.5)

    def eventLoopProcessing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    self.game = GridClass(2.5)
                    self.win = False
                if event.key == pygame.K_UP and self.win == False:
                    self.game.moveUp()
                if event.key == pygame.K_DOWN and self.win == False:
                    self.game.moveDown()
                if event.key == pygame.K_RIGHT and self.win == False:
                    self.game.moveRight()
                if event.key == pygame.K_LEFT and self.win == False:
                    self.game.moveLeft()
                if event.key == pygame.K_SPACE and self.win == False:
                    self.game.update()

    def checkWinCondition(self):
        if self.win == False:
            self.win = self.game.checkWin()

    def drawGame(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslate(0.0, 0.0, -20.0)

        self.game.draw()

        pygame.display.flip()

