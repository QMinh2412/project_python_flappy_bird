import pygame

class Bird:
    def __init__ (bird):
        bird_img = pygame.image.load('assets/sprites/redbird-midflap.png').convert()
        bird_img = pygame.transform.scale2x(bird_img)
        bird.image = bird_img
        bird.rect = bird.image.get_rect(center=(100,384))
        bird.gravity = 0.25
        bird.movement = 0
        bird.jump_strength = -8

    def update(bird):
        bird.movement = bird.movement + bird.gravity
        bird.rect.centery = bird.rect.centery + bird.movement

    def jump(bird):
        bird.movement = bird.jump_strength

    def draw(bird, screen):
        screen.blit(bird.image, bird.rect)