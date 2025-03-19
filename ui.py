import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.bg = pygame.image.load('assets/sprites/background-night.png')
        self.bg = pygame.transform.scale(self.bg, (432, 700))
        self.floor = pygame.image.load('assets/sprites/base.png')
        self.floor = pygame.transform.scale2x(self.floor)
        self.floor_x_pos = 0

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def draw_floor(self):
        self.screen.blit(self.floor, (self.floor_x_pos, 550))
        self.screen.blit(self.floor, (self.floor_x_pos + 432, 550))

    def floor_loop(self):
        self.floor_x_pos -= 1
        if self.floor_x_pos <= -432:
            self.floor_x_pos = 0