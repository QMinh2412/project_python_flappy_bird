import pygame

class Pipe:
    def __init__(self):
        self.pipe_green = pygame.image.load('assets/sprites/pipe-green.png').convert()
        self.pipe_green = pygame.transform.scale2x(self.pipe_green)
        self.pipe_green_list = []
        self.spawn_pipe_green = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_pipe_green, 1200)

    def create_pipe(self):
        new_pipe = self.pipe_green.get_rect(midtop=(500, 384))
        return new_pipe

    def move_pipe(self):
        for pipe in self.pipe_green_list:
            pipe.centerx -= 5

    def draw_pipe(self, screen):
        for pipe in self.pipe_green_list:
            screen.blit(self.pipe_green, pipe)