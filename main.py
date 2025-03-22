# pylint: disable=no-member
import pygame, sys
from bird import Bird
from ui import UI

# Hàm kiểm tra va chạm với ống và sàn
def check_collision():
    # for pipe in pipes:
    #     if bird_img.colliderect(pipe):
    #         print('va cham')
    if bird.rect.top <= -75 or bird.rect.bottom >= 550:
        return False
    return True

pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0,0,0))
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tốc độ khung hình
    pygame.display.update()
    clock.tick(60)

pygame.quit()