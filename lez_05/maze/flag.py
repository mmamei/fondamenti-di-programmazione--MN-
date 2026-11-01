import pygame
from constants import *
flag_image = pygame.image.load('lez_6/maze/images/flag.png')

def create_flag():
    tmp_image = pygame.transform.scale(flag_image, (WALL_DX,WALL_DY))
    surf = tmp_image.convert()
    rect = surf.get_rect()
    rect.left = SCREEN_WIDTH - 1 * WALL_DX
    rect.top = SCREEN_HEIGHT - 2 * WALL_DY
    return {"surf": surf, "rect": rect}
