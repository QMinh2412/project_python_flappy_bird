# pylint: disable=no-member
import pygame

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
running = True

while running:
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()