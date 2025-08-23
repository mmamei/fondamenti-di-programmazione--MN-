import pygame
from pygame.locals import *
from constants import *


player_image = pygame.image.load('maze/images/tank1.png')
player_image = pygame.transform.scale(player_image, (WALL_DX*0.8,WALL_DY*0.8))

def create_player():
    surf = pygame.transform.rotate(player_image, 90)
    rect = surf.get_rect()
    rect.center = [10, WALL_DY + WALL_DY/2]
    return {"surf": surf, "rect": rect, "v": 3, "direction": 90}

def update_player(player, pressed_keys, wall_list, flag):
    dx = 0
    dy = 0
    if pressed_keys[K_UP]:
        dy = -player["v"]
        player["direction"] = 180
    if pressed_keys[K_DOWN]:
        dy = player["v"]
        player["direction"] = 0
    if pressed_keys[K_LEFT]:
        dx  = -player["v"]
        player["direction"] = 270
    if pressed_keys[K_RIGHT]:
        dx = player["v"]
        player["direction"] = 90
    player["surf"] = pygame.transform.rotate(player_image, player["direction"])
    player["rect"].move_ip(dx,dy)
    # Keep player on the screen
    if player["rect"].left < 0:
        player["rect"].left = 0
    elif player["rect"].right > SCREEN_WIDTH:
        player["rect"].right = SCREEN_WIDTH
    if player["rect"].top <= 0:
        player["rect"].top = 0
    elif player["rect"].bottom >= SCREEN_HEIGHT:
        player["rect"].bottom = SCREEN_HEIGHT
    # Wall collision
    for wall in wall_list:
        if player["rect"].colliderect(wall["rect"]):
            player["rect"].move_ip(-dx,-dy)
    # Win condition

    if player["rect"].colliderect(flag["rect"]):
        return True
    return False
