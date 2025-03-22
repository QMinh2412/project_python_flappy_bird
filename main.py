# pylint: disable=no-member
import pygame
from pipe import Pipe

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
running = True

pipe_manager = Pipe()

while running:
    screen.fill((0,0,0))
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pipe_manager.spawn_pipe_green:
            pipe_manager.pipe_green_list.append(pipe_manager.create_pipe())

    pipe_manager.move_pipe()
    pipe_manager.draw_pipe(screen)

    # Tốc độ khung hình
    pygame.display.update()
    clock.tick(60)

pygame.quit()