import os 
import random 
import math 
import pygame
from os import listdir
from os.path import isfile, join

class Player(pygame.sprite.Sprite):

    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.xVelocity = 0
        self.yVelocity = 0
        self.mask = None
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, velocity):
        self.xVelocity = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animationCount = 0

    def move_right(self, velocity):
        self.xVelocity = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
        
    def loop(self, fps):
        self.move(self.xVelocity, self.yVelocity)
    
    def drawImage(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
