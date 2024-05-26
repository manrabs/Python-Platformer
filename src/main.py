import os 
import random 
import math 
import pygame
from utils.Player import Player
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platform Guy")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VELOCITY = 7

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            position = (i * width, j * height)
            tiles.append(position)
            
    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    
    player.drawSprite(window)
    pygame.display.update()

def moveDirection(player):
    #set velocity to 0 to ensure player only moves on key press
    player.xVelocity = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)

def main(window):

    #set up fps and event quitting to end game upon user exit i.e. clicking 'x' button
    clock = pygame.time.Clock()
    background, bg_image = get_background("Yellow.png")

    player = Player(50, 50, 25, 25)

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        moveDirection(player)
        draw(window, background, bg_image, player)
    pygame.quit()
    quit()

    pass

if __name__ == "__main__":
    main(window)