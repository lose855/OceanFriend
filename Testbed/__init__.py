import pygame
pygame.init()

class Target:
    def __init__(self):
        self.shape = pygame.image.load('target.png')
        self.speed = 1
        self.x = 100
        self.y = 1000

class Testbed:

    class Move:
        def __init__(self, target, testbed):
            self.target = target
            self.testbed = testbed
            self.head = 'horizon'

        def updte(self):
            self.testbed.blit(self.target.shape, (self.target.x, self.target.y))

        def foward(self, power):
            if self.head == 'horizon':
                for i in range(int(power/self.target.speed)):
                    self.target.x += self.target.speed
                    self.updte()
            else:
                for i in range(int(power/self.target.speed)):
                    self.target.y += self.target.speed
                    self.updte()
            return self.target

        def rotate(self, direction):
            if direction == 'normal':


    def __init__(self):
        self.size = [1920, 1080]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Testbed")
