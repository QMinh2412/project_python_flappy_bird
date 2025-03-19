import pygame
import random

pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
running = True
pipe_green = pygame.image.load('assets/sprites/pipe-green.png').convert()
pipe_green = pygame.transform.scale2x()
pipe_green_pos = 0
spawn_pipe_green = pygame.USEREVENT
pygame.time.set_timer(spawn_pipe_green, 1200)

pipe_green_list = []

def create_pipe():
    new_pipe = pipe_green.get_rect(midtop=(500,384))
    return new_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        screen.blit(pipe_green, pipe)


while running:
    screen.fill((0, 0, 0))
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_pipe_green:
            pipe_green_list.append(create_pipe())
        
    pipe_green_list = move_pipe(pipe_green_list)
    draw_pipe(pipe_green_list) 
    
    
    
    
    
    pygame.display.update()
    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()

