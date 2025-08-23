import pygame

flag_image = pygame.image.load('maze/images/flag.png')

def create_flag(x, y, dx, dy):
    tmp_image = pygame.transform.scale(flag_image, (dx,dy))
    surf = tmp_image.convert()
    rect = surf.get_rect()
    rect.left = x
    rect.top = y
    return {"surf": surf, "rect": rect}
