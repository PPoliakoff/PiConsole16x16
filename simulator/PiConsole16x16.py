import pygame
import sys


class PiConsole16x16:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((512, 512))
        pygame.display.set_caption('PiConsole16x16')
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        self.clear()
        self.refresh()

    def clear(self):
        self.mat = [[0 for _ in range(16)] for _ in range(16)]

    def refresh(self):
        self.mouse = pygame.mouse.get_rel()
        self.screen.fill((0, 0, 0))
        for r in range(16):
            for c in range(16):
                status = (192, 0, 0) if self.mat[c][r] else (40, 40, 40)
                pygame.draw.circle(self.screen, status,
                                   (c*32+16, r*32+16), 14)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()

    def setPixel(self, x, y, c):
        self.mat[x][y] = c != 0

    def getPixel(self, x, y):
        return self.mat[x][y]

    def joyX(self):
        retval= (self.mouse[0]+5)//10
        if retval<-7:
            retval=-7
        elif retval>8:
            retval=8
        return retval

    def joyY(self):
        retval= (self.mouse[1]+5)//10
        if retval<-7:
            retval=-7
        elif retval>8:
            retval=8
        return retval
