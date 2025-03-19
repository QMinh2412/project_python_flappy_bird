import pygame, sys
from bird import Bird
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/sprites/background-day.png')
bg = pygame.transform.scale2x(bg)

bird_img = pygame.image.load('assets/sprites/redbird-midflap.png').convert()
bird_img = pygame.transform.scale2x(bird_img)

bird = Bird(100, 384, bird_img)

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


    bird.update()
    screen.blit(bg,(0,0))
    bird.draw(screen)
    pygame.display.update()
    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()