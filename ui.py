import pygame, sys

def floor_loop():
    screen.blit(floor,(floor_x_pos,550))
    screen.blit(floor,(floor_x_pos+432,550))

pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
bg = pygame.image.load('assets/sprites/background-night.png')
bg = pygame.transform.scale(bg,(432,700))
floor = pygame.image.load('assets/sprites/base.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

running = True

while running:
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    screen.blit(bg,(0,0))
    floor_x_pos -= 1
    floor_loop()
    if floor_x_pos <= -432:
        floor_x_pos = 0
   
    pygame.display.update()
    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()