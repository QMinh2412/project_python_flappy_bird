import pygame, sys
from bird import Bird
from ui import UI
from pipe import Pipe

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((432, 720))
clock = pygame.time.Clock()
running = True

# Khởi tạo các đối tượng duy nhất
pipe = Pipe()
ui = UI(screen)
bird = Bird()

# Hàm kiểm tra va chạm với ống và sàn
def check_collision(pipes):
    for bottom, top, score_rect, passed in pipes:
        # Kiểm tra va chạm với ống
        if bird.rect.colliderect(bottom) or bird.rect.colliderect(top):
            ui.hit_sound.play()
            ui.die_sound.play()
            return False

        # Kiểm tra nếu chim vượt qua ống và chưa tính điểm
        if bird.rect.left > score_rect.right and not passed:
            ui.score += 1  # Cộng điểm
            pipes[pipes.index((bottom, top, score_rect, passed))] = (bottom, top, score_rect, True)  # Cập nhật trạng thái
            ui.point_sound.play()           

    # Kiểm tra va chạm với sàn hoặc trần
    if bird.rect.top <= -75 or bird.rect.bottom >= 550:
        ui.hit_sound.play()
        ui.die_sound.play()
        return False

    return True


game_active = False

while running:
    # Xử lý sự kiện quit và các sự kiện khác
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP) and game_active:
                bird.jump()
                ui.flap_sound.play()
            if event.key in (pygame.K_SPACE, pygame.K_UP) and game_active == False:
                game_active = True
                pipe.pipe_list.clear()
                bird.restart()
                ui.score = 0
                ui.passed= False

        if event.type == pipe.spawn_pipe:
            pipe.pipe_list.append(pipe.create_pipe())
            # ui.pipe_spawned = True     

        if event.type == bird.BIRDFLAP_EVENT:
            if bird.bird_index < 2:
                bird.bird_index += 1
            else:
                bird.bird_index = 0
            bird.animation()
        
    ui.background()

    # Nếu game đang chạy
    if game_active:
    # Update bird and pipes
        bird.update()
        bird.rotate()
        bird.draw(screen)
        pipe.move_pipe()
        pipe.draw_pipe(screen)

        # Check for collisions and update game state
        game_active = check_collision(pipe.pipe_list)

        # Display the score
        ui.score_display('main game')

    else:
        # Update high score and display game over screen
        ui.update_score()
        ui.score_display('game over')

    # Cập nhật giao diện sàn
    ui.floor_loop()
    ui.draw_floor()
    pygame.display.update()
    clock.tick(60)

pygame.quit()  