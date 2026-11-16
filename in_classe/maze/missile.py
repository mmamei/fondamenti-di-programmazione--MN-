import pygame
from pygame.locals import *
from constants import *


boom_image = pygame.image.load('lez_05/maze/images/boom.png')
boom_image = pygame.transform.scale(boom_image, (WALL_DX*0.8,WALL_DY*0.8))
boom_image.set_colorkey(boom_image.get_at((0, 0)))

missile_image = pygame.image.load('lez_05/maze/images/missile.png')
missile_image = pygame.transform.scale(missile_image, (WALL_DX*0.8,WALL_DY*0.8))
missile_image.set_colorkey(missile_image.get_at((0, 0)))

def create_missile(center, direction):
    surf = pygame.transform.rotate(missile_image, direction - 90)
    rect = surf.get_rect()
    rect.center = center
    return {
        "surf": surf,
        "rect": rect,
        "v": 6,
        "direction": direction,
        'running':True,
        'exploding_time':20
    }

def update_missile(missile, wall_list, flag):

    if not missile['running']:
        missile['surf'] = pygame.transform.rotate(boom_image, missile["direction"])
        missile['exploding_time'] -= 1
    else:
        direction = missile["direction"]
        speed = missile["v"]
        dx, dy = {
            0: (0, speed),
            90: (speed, 0),
            180: (0, -speed),
            270: (-speed, 0),
        }[direction]
        
        missile["rect"].move_ip(dx, dy)

        for wall in wall_list:
            if missile["rect"].colliderect(wall["rect"]):
                missile["running"] = False
                break
