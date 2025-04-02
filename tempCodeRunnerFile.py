         pipe_rect, passed = pipe.pipe_list[i]
            if pipe_rect.centerx < bird.rect.centerx and not passed:
                pipe.pipe_list[i] = (pipe_rect, True)  # Đánh dấu đã vượt qua
                ui.point_sound.play()  # Phát âm thanh đúng lúc
                ui.score += 1  # Tăng điểm