# pylint: disable=no-member
import pygame, sys
from bird import Bird
from ui import UI

pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()

ui = UI(screen)

bird_img = pygame.image.load('assets/sprites/redbird-midflap.png').convert()
bird_img = pygame.transform.scale2x(bird_img)

bird = Bird()

running = True

while running:
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.K_UP:
                bird.jump()

    ui.background()
    ui.floor_loop()
    ui.draw_floor()

    bird.update()
    bird.draw(screen)
    pygame.display.update()

    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()