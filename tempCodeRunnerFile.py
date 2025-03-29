if event.key in (pygame.K_SPACE, pygame.K_UP) and game_active == False:
                game_active = True
                pipe.pipe_list.clear()
                bird.restart()
                ui.score = 0