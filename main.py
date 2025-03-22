# pylint: disable=no-member
import pygame, sys
from bird import Bird
from ui import UI
from pipe import Pipe

pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
running = True

ui = UI(screen)
bird = Bird()
pipe = Pipe()

# Hàm kiểm tra va chạm với ống và sàn
def check_collision(pipes):
    for pipe in pipes:
        if bird.rect.colliderect(pipe):
            return False
    if bird.rect.top <= -75 or bird.rect.bottom >= 550:
        return False
    return True

game_active = True

while running:
    # Xử lý sự kiện quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP) and game_active:
                bird.jump()
            if event.key in (pygame.K_SPACE, pygame.K_UP) and game_active == False:
                game_active = True
                bird.restart()

        if event.type == pipe.spawn_pipe_green:
            pipe.pipe_green_list.append(pipe.create_pipe())

    # Kiểm tra game đang chạy không, nếu va chạm sẽ ngưng
    if game_active:
        # bird
        bird.update()
        bird.draw(screen)

        #pipe
        pipe.draw_pipe(screen)
        pipe.move_pipe()
        
        game_active = check_collision(pipe.pipe_green_list)

        pygame.display.update()

    # UI
    ui.background()
    ui.floor_loop()
    ui.draw_floor()

    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()