# pylint: disable=no-member
import pygame, sys


from ui import UI

from bird import Bird
pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/sprites/background-day.png')
bg = pygame.transform.scale2x(bg)

running = True

ui = UI(screen)
bird = Bird()

game_active = True

while running:
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_SPACE or pygame.K_UP) and game_active:
                bird.jump()
            if event.key == (pygame.K_SPACE or pygame.K_UP) and game_active == False:
                game_active = True
                bird.restart()


    bird.update()
    screen.blit(bg,(0,0))
    bird.draw(screen)
    pygame.display.update()
    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()