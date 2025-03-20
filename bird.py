import pygame

class Bird:
    def __init__ (self, x, y, image):
        self.image = image
        self.rect = image.get_rect(center=(x,y))
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