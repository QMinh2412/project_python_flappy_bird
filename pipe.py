import pygame, random

class Pipe:
    def __init__(self):
        self.pipe_img = pygame.image.load('assets/sprites/pipe-green.png').convert()
        self.pipe_img = pygame.transform.scale2x(self.pipe_img)
        self.pipe_list = []
        self.pipe_height = [200, 300, 400]
        self.spawn_pipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_pipe, 1200)

    def create_pipe(self):
        random_pipes_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_img.get_rect(midtop=(500, random_pipes_pos))
        top_pipe = self.pipe_img.get_rect(midtop=(500, random_pipes_pos-800))
        return bottom_pipe, top_pipe

    def move_pipe(self):
        self.pipe_list = [pipe for pipe in self.pipe_list if pipe.right > 0]
        for pipe in self.pipe_list:
            pipe.centerx -= 5

    def draw_pipe(self, screen):
        for pipe in self.pipe_list:
            if pipe.bottom > 720:
                screen.blit(self.pipe_img, pipe)
            else:
                flip_pipe = pygame.transform.flip(self.pipe_img, False, True)
                screen.blit(flip_pipe, pipe)
