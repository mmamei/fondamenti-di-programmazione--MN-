import pygame
from pygame.locals import *
import random
from pygame import font
from constants import *
from player import *
from wall import *
from flag import create_flag
from maze import create_maze

num_enemy_killed = 0
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
maze = None
running = True
gameon = False

player = create_player()
flag = create_flag(SCREEN_WIDTH - 1* WALL_DX, SCREEN_HEIGHT - 2* WALL_DY , WALL_DX, WALL_DY)  
wall_list = []

clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_1:
                gameon = True
        elif event.type == QUIT:
            running = False
    screen.fill([0, 0, 0])
    if not gameon:
        surf = font.Font(None,36).render('Premi 1 per iniziare...', True, [255,255,255])
        screen.blit(surf, (SCREEN_WIDTH/2-surf.get_width()/2, SCREEN_HEIGHT/2))
        if maze == None:
            player = create_player()
            wall_list = create_maze()
    if gameon:
        win = update_player(player, pygame.key.get_pressed(), wall_list, flag)
        
        # draw elements
        for wall in wall_list:
            screen.blit(wall["surf"], wall["rect"])
        screen.blit(player["surf"], player["rect"])
        screen.blit(flag["surf"], flag["rect"])

        if win:
            gameon = False
            maze = None
    pygame.display.flip()
    clock.tick(200)



