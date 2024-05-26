import os 
import random 
import math 
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()


WIDTH, HEIGHT = 1000, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Flip sprites in opposite (X-axis) direction
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(fol1, fol2, width, height, direction=False):
    path = join("assets", fol1, fol2)
    images = [file for file in listdir (path) if isfile(join(path, file))]

    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i*width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] + sprites

    return all_sprites

class Player(pygame.sprite.Sprite):

    # COLOR = (255, 0, 0)
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "VirtualGuy", 32, 32, True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.xVelocity = 0
        self.yVelocity = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
    
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
        # Line 73 increases y velocity by gravity for each frame in loop (i.e. each frame in screen)
        # self.yVelocity += min(1, (self.fall_count/fps) * self.GRAVITY)

        self.move(self.xVelocity, self.yVelocity)
        self.fall_count += 1

    def drawSprite(self, window):
        # pygame.draw.rect(window, self.COLOR, self.rect)
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        window.blit(self.sprite, (self.rect.x, self.rect.y))
