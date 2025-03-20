import pygame, sys


from ui import UI

from bird import Bird

pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()

ui = UI(screen)

bird = Bird(screen)

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