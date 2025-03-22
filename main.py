
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

    # Kiểm tra game đang chạy không, nếu va chạm sẽ ngưng
    if game_active:
        # bird
        bird.update()
        bird.draw(screen)
        game_active = check_collision()
        pygame.display.update()

    # UI
    ui.background()
    ui.floor_loop()
    ui.draw_floor()

    # Tốc độ khung hình
    clock.tick(60)

pygame.quit()
