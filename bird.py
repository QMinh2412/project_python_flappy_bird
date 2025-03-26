# pylint: disable=no-member
import pygame

class Bird:
    def __init__ (self):
        self.bird_index = 0
        upflap = pygame.transform.scale2x(pygame.image.load('assets/sprites/redbird-upflap.png').convert_alpha())
        midflap = pygame.transform.scale2x(pygame.image.load('assets/sprites/redbird-midflap.png').convert_alpha())
        downflap = pygame.transform.scale2x(pygame.image.load('assets/sprites/redbird-downflap.png').convert_alpha())
        self.images = [upflap, midflap, downflap]
        self.current_image = self.images[self.bird_index]
        self.rect = self.current_image.get_rect(center=(100,384))
        self.gravity = 0.25
        self.movement = 0
        self.jump_strength = -6.5
        self.BIRDFLAP_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.BIRDFLAP_EVENT, 200)

    def update(self):
        self.movement = self.movement + self.gravity
        self.rect.centery = self.rect.centery + self.movement

    def jump(self):
        self.movement = self.jump_strength

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)

    def rotate(self):
        self.rotated_image = pygame.transform.rotozoom(self.current_image, -self.movement * 3, 1)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)

    def animation(self):
        self.current_image = self.images[self.bird_index]
        self.rotate()
    
    def restart(self):
        self.rect.center = (100, 384)
        self.movement = 0
        self.bird_index = 0
        self.animation()