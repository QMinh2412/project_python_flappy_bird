# pylint: disable=no-member
import pygame, sys

from ui import UI

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
ui = UI(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    ui.background()
    ui.floor_loop()
    ui.draw_floor()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()