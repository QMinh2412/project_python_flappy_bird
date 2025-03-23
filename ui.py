import pygame

class UI:
    def __init__(self, screen):
        #font game
        self.game_font = pygame.font.Font('04B_19.ttf', 40)
        #background, san
        self.screen = screen
        self.bg = pygame.image.load('assets/sprites/background-night.png')
        self.bg = pygame.transform.scale(self.bg, (432, 700))
        self.floor = pygame.image.load('assets/sprites/base.png')
        self.floor = pygame.transform.scale2x(self.floor)
        self.floor_x_pos = 0
        #score
        self.score = 0
        self.high_score = 0

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 550))
        self.screen.blit(self.floor, (self.floor_x_pos + 432, 550))

    def floor_loop(self):
        self.floor_x_pos -= 1
        if self.floor_x_pos <= -432:
            self.floor_x_pos = 0

    def score_display(self):
        self.score_surface = self.game_font.render(str(self.score), True, (255, 255, 255))
        self.score_rect = self.score_surface.get_rect(center = (216, 100))
        self.screen.blit(self.score_surface, self.score_rect)

    def update_score(self, bird, pipes):
        for pipe in pipes:
            if pipe.centerx < bird.rect.left and not pipe.passed:
                self.score +=1
                pipe.passed = True