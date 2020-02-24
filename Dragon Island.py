# -*- coding:utf-8 -*-
# 图形界面版 vertion 0.5.0a1

import pygame
from pygame.locals import *
import os

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FRAME_WIDTH = 3

BG_COLOR1 = (21, 35, 50)
FRAME_COLOR = (60, 60, 60)
BG_COLOR2 = (220, 220, 220)


if __name__ == '__main__':
    # 设置运行环境
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    os.chdir(current_dir)  # 切换工作目录到当前文件目录，方便加载资源
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # 使Pygame窗体居中

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    surf_main = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT * 2 / 3))
    surf_main.fill(BG_COLOR1)
    rect_main = surf_main.get_rect()
    surf_input = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 3 - FRAME_WIDTH))
    surf_input.fill(BG_COLOR1)
    rect_input = surf_input.get_rect().move(0, SCREEN_HEIGHT * 2 / 3 + FRAME_WIDTH)
    surf_role = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2))
    surf_role.fill(BG_COLOR1)
    rect_role = surf_role.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, 0)
    surf_monster = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2 - FRAME_WIDTH))
    surf_monster.fill(BG_COLOR1)
    rect_monster = surf_monster.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, SCREEN_HEIGHT / 2 + FRAME_WIDTH)

    pygame.display.set_caption('Dragon Island 1.0')
    icon = pygame.image.load('./res/icon.png')
    pygame.display.set_icon(icon)

    surf_bg = pygame.Surface(SCREEN_SIZE)
    surf_bg.fill(FRAME_COLOR)
    
    # 绘制边框
    pygame.draw.line(surf_bg, FRAME_COLOR, (SCREEN_WIDTH * 2 / 3, 0), (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT), FRAME_WIDTH)
    pygame.draw.line(surf_bg, FRAME_COLOR, (0, SCREEN_HEIGHT * 2 / 3), (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT * 2 / 3), FRAME_WIDTH)
    pygame.draw.line(surf_bg, FRAME_COLOR, (SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2), FRAME_WIDTH)
    
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
        screen.blit(surf_bg, (0, 0))
        screen.blit(surf_main, rect_main)
        screen.blit(surf_input, rect_input)
        screen.blit(surf_role, rect_role)
        screen.blit(surf_monster, rect_monster)

        text_obj = font.render('白龙马', True, (255, 255, 255))
        screen.blit(text_obj, (600, 320))

        pygame.display.flip()

    pygame.quit()
