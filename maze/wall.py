import pygame

wall_image = pygame.image.load('maze/images/wall.png')

def create_wall(x, y, dx, dy):
    tmp_image = pygame.transform.scale(wall_image, (dx,dy))
    surf = tmp_image.convert()
    rect = surf.get_rect()
    rect.left = x
    rect.top = y
    return {"surf": surf, "rect": rect}
