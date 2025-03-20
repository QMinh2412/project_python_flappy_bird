import pygame

class Bird:
    def __init__ (self):
        bird_img = pygame.image.load('assets/sprites/redbird-midflap.png').convert()
        bird_img = pygame.transform.scale2x(bird_img)
        self.image = bird_img
        self.rect = self.image.get_rect(center=(100,384))
        self.gravity = 0.25
        self.movement = 0
        self.jump_strength = -8

    def update(self):
        self.movement = self.movement + self.gravity
        self.rect.centery = self.rect.centery + self.movement

    def jump(self):
        self.movement = self.jump_strength

    def draw(self, screen):
        screen.blit(self.image, self.rect)