import pygame
from pygame.locals import *
from constants import *


missile_image = pygame.image.load('lez_05/maze/images/missile.png')
missile_image = pygame.transform.scale(missile_image, (WALL_DX*0.8,WALL_DY*0.8))
missile_image.set_colorkey(missile_image.get_at((0, 0)))

def create_missile(player):
    surf = pygame.transform.rotate(missile_image, player["direction"]-90)
    rect = surf.get_rect()
    rect.center = player["rect"].center
    return {
        "surf": surf,
        "rect": rect,
        "v": 3,
        "direction": player["direction"],
    }

def update_missile(missile, wall_list, flag):
    direction = missile["direction"]
    speed = missile["v"]
    dx, dy = {
        0: (0, speed),
        90: (speed, 0),
        180: (0, -speed),
        270: (-speed, 0),
    }[direction]
    #missile["surf"] = pygame.transform.rotate(missile_image, missile["direction"])
    missile["rect"].move_ip(dx, dy)
