# -*- coding:utf-8 -*-
# 图形界面版 vertion 0.5.0a1

import pygame
from pygame.locals import *
import os

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BG_COLOR = (21, 35, 50)
FRAME_COLOR = (60, 60, 60)
FRAME_WIDTH = 3

if __name__ == '__main__':
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    os.chdir(current_dir)

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Dragon Island 1.0')
    
    bg_surf = pygame.Surface(SCREEN_SIZE)
    bg_surf.fill(BG_COLOR)
    # 绘制边框
    pygame.draw.line(bg_surf, FRAME_COLOR, (SCREEN_WIDTH * 2 / 3, 0), (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT), FRAME_WIDTH)
    pygame.draw.line(bg_surf, FRAME_COLOR, (0, SCREEN_HEIGHT * 2 / 3), (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT * 2 / 3), FRAME_WIDTH)
    pygame.draw.line(bg_surf, FRAME_COLOR, (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2), FRAME_WIDTH)
    
    clock = pygame.time.Clock()
    font = pygame.font.Font('./res/PingFang.ttc', 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        clock.tick(120)
        screen.blit(bg_surf, (0, 0))
        text_obj = font.render('白龙马', True, (255, 255, 255))
        screen.blit(text_obj, (600, 320))
        
        pygame.display.flip()

    pygame.quit()
