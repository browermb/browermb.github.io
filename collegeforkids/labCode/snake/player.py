from pygame.locals import *
import pygame

class Player:
    x = []
    y = []
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        #for loop that will run length number of times
            self.x.append(0)
            self.y.append(0)

    def update(self):
        self.updateCount = self.updateCount + 1
        
        #update previous positions
        """If statetment so that the code only 
            happens if updateCount is less than or 
            equal to updateCountMax"""
        #If statement goes here
            for i in range(self.length -  1, 0 , -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            #update position of head of snake
            # write an if statement to check if direction is 0
                self.x[0] = self.x[0] + self.step
            # write an if statement to check if direction is 1
                self.x[0] = self.x[0] - self.step
            # write an if statement to check if direction is 2
                self.y[0] = self.y[0] - self.step
            # write an if statement to check if direction is 3
                self.y[0] = self.y[0] + self.step

            #set the value of self.updateCount to 0

    """
    define and finish three functions called: moveLeft, moveUp, moveDown
    moveLeft should set direction to 1
    moveUp should set direction to 2
    moveDOwn should set direction to 3
    """
    def moveRight(self):
        self.direction = 0

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))