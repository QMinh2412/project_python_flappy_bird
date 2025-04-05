import pygame

class UI:
    def __init__(self, screen):
        # Font game
        self.game_font = pygame.font.Font('assets/fonts/04B_19.ttf', 40)
        # Background và sàn
        self.screen = screen
        self.bg = pygame.image.load('assets/sprites/background-night.png')
        self.bg = pygame.transform.scale(self.bg, (432, 700))
        self.floor = pygame.image.load('assets/sprites/base.png')
        self.floor = pygame.transform.scale2x(self.floor)
        self.floor_x_pos = 0
        # Score
        self.pipe_spawned = False
        self.score = 0
        self.high_score = 0
        # Màn hình kết thúc game
        self.game_over_surface = pygame.image.load('assets/sprites/message_resized.png').convert_alpha()
        self.game_over_surface = pygame.transform.scale(self.game_over_surface, (250, 350)) 
        self.game_over_rect = self.game_over_surface.get_rect(center=(216, 300))
        #chèn âm thanh
        self.flap_sound = pygame.mixer.Sound('assets/audio/sfx_wing.wav')
        self.flap_sound.set_volume(0.1)
        self.hit_sound = pygame.mixer.Sound('assets/audio/sfx_hit.wav')
        self.hit_sound.set_volume(0.1)
        self.point_sound = pygame.mixer.Sound('assets/audio/sfx_point.wav')
        self.point_sound.set_volume(0.1)
        self.score_sound_countdown = 100
        self.die_sound = pygame.mixer.Sound('assets/audio/sfx_die.wav')
        self.die_sound.set_volume(0.1)

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 550))
        self.screen.blit(self.floor, (self.floor_x_pos + 432, 550))

    def floor_loop(self):
        self.floor_x_pos -= 1
        if self.floor_x_pos <= -432:
            self.floor_x_pos = 0

    def score_display(self, game_state):
        if game_state == 'main game':
            # Hiển thị màn hình đang chơi
            score_surface = self.game_font.render(f'{int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(216, 100))
            self.screen.blit(score_surface, score_rect)

        elif game_state == 'game over':
            # Hiển thị màn hình kết thúc
            self.screen.blit(self.game_over_surface, self.game_over_rect)

            # Hiển thị điểm
            score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(216, 80))
            self.screen.blit(score_surface, score_rect)

            # Hiển thị điểm cao nhất
            high_score_surface = self.game_font.render(f'High Score: {int(self.high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(216, 500))
            self.screen.blit(high_score_surface, high_score_rect)

    def update_score(self):
        # cập nhật lại điểm
        if self.score > self.high_score:
            self.high_score = self.score
