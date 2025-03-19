import pygame

class Bird:
    def __init__ (bird, x, y, image):
        bird.image = image
        bird.rect = image.get_rect(center=(x,y))
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