# pylint: disable=no-member
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
    for pipe in pipes:
        if bird.rect.colliderect(pipe):
            ui.hit_sound.play()
            ui.die_sound.play()
            return False
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
                ui.pipe_spawned= False

        if event.type == pipe.spawn_pipe:
            pipe.pipe_list.extend(pipe.create_pipe())
            ui.pipe_spawned = True     

        if event.type == bird.BIRDFLAP_EVENT:
            if bird.bird_index < 2:
                bird.bird_index += 1
            else:
                bird.bird_index = 0
            bird.animation()
        
    ui.background()

    # Nếu game đang chạy
    if game_active:
        # Chim
        bird.update()
        bird.rotate()
        bird.draw(screen)
        # Ống
        pipe.move_pipe()
        pipe.draw_pipe(screen)
        #check va chạm
        game_active = check_collision(pipe.pipe_list)
        #điểm
        ui.score_display('main game')
        ui.score_sound_countdown -=1
        if ui.score_sound_countdown <=0:
            ui.point_sound.play()
            ui.score_sound_countdown = 100
    else:
        # Cập nhật high score và hiển thị màn hình game over
        ui.high_score = ui.update_score(ui.score, ui.high_score)
        ui.score_display('game over')

    # Cập nhật giao diện sàn
    ui.floor_loop()
    ui.draw_floor()
    pygame.display.update()
    clock.tick(60)

pygame.quit()  