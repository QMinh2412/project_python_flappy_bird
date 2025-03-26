# pylint: disable=no-member
import pygame, sys
from bird import Bird
from ui import UI
from pipe import Pipe


# Hàm kiểm tra va chạm với ống và sàn
def check_collision():
    # for pipe in pipes:
    #     if bird.rect.colliderect(pipe):
    #          return False
    if bird.rect.top <= -75 or bird.rect.bottom >= 550:
        return False
    return True

pygame.init()
screen = pygame.display.set_mode((432,720))
clock = pygame.time.Clock()
running = True


pipe = Pipe()
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

        if event.type == pipe.spawn_pipe:
            pipe.pipe_list.extend(pipe.create_pipe())       

        if event.type == bird.BIRDFLAP_EVENT:
            if bird.bird_index < 2:
                bird.bird_index += 1
            else:
                bird.bird_index = 0
            bird.animation()
       
    

    ui.background()

    # Kiểm tra game đang chạy không, nếu va chạm sẽ ngưng
    if game_active:
        bird.update()
        bird.rotate()
        bird.draw(screen)
        pipe.move_pipe()
        pipe.draw_pipe(screen)
        game_active = check_collision()

    # UI
    ui.floor_loop()
    ui.draw_floor()
    #ui.update_score(bird, pipe)
    ui.score_display()
    ui.update_score(bird, pipe.pipe_list)

    pygame.display.update()

    clock.tick(60)

pygame.quit()