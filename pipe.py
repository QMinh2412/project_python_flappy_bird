import pygame, random

class Pipe:
    def __init__(self):
        self.pipe_img = pygame.image.load('assets/sprites/pipe-green.png').convert()
        self.pipe_img = pygame.transform.scale2x(self.pipe_img)
        self.pipe_list = []
        self.pipe_height = [200, 300, 400]
        self.spawn_pipe = pygame.USEREVENT
        pygame.time.set_timer(self.spawn_pipe, 1400)

    def create_pipe(self):
        random_pipes_pos = random.choice(self.pipe_height)
        bottom_pipe = self.pipe_img.get_rect(midtop=(500, random_pipes_pos))
        top_pipe = self.pipe_img.get_rect(midtop=(500, random_pipes_pos - 800))
        
        # Score Rect: Một hitbox nhỏ có chiều rộng 1px, chiều cao full màn hình
        score_rect = pygame.Rect(bottom_pipe.right, 0, 1, 720)

        return bottom_pipe, top_pipe, score_rect, False  # Thêm 'False' để đánh dấu trạng thái tính điểm
    def move_pipe(self):
        new_pipes = []
        for bottom, top, score, passed in self.pipe_list:
            if bottom.right > 0:
                new_pipes.append((bottom, top, score, passed))  # Giữ nguyên tất cả giá trị
        
        self.pipe_list = new_pipes
        for bottom, top, score, passed in self.pipe_list:
            bottom.centerx -= 5
            top.centerx -= 5
            score.centerx -= 5


    def draw_pipe(self, screen):
        for bottom, top, _, _ in self.pipe_list:  # Thêm biến 'passed' nhưng không sử dụng
            screen.blit(self.pipe_img, bottom)
            flip_pipe = pygame.transform.flip(self.pipe_img, False, True)
            screen.blit(flip_pipe, top)
