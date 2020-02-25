# -*- coding:utf-8 -*-
# 图形界面版 vertion 0.5.0a1

import os

import pygame
from pygame.locals import *

# Constants
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FRAME_WIDTH = 3

FRAME_COLOR = (60, 60, 60)
BG_COLOR1 = (21, 35, 50)    
BG_COLOR2 = (220, 220, 220)


class Game(object):

    def __init__(self):
        # 设置运行环境
        cur_dir = os.path.split(os.path.abspath(__file__))[0]
        os.chdir(cur_dir)  # 切换工作目录到当前文件目录，方便加载资源
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # 使Pygame窗体居中

        # Pygame初始化
        pygame.init()
        pygame.display.set_caption('Dragon Island 1.0')
        icon = pygame.image.load('./res/icon.png')
        pygame.display.set_icon(icon)

        self._screen = pygame.display.set_mode(SCREEN_SIZE)

        self._surf_main = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT * 2 / 3))
        self._surf_main.fill(BG_COLOR1)
        self._rect_main = self._surf_main.get_rect()

        self._surf_input = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 3 - FRAME_WIDTH))
        self._surf_input.fill(BG_COLOR1)
        self._rect_input = self._surf_input.get_rect().move(0, SCREEN_HEIGHT * 2 / 3 + FRAME_WIDTH)

        self._surf_role = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2))
        self._surf_role.fill(BG_COLOR1)
        self._rect_role = self._surf_role.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, 0)

        self._surf_monster = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2 - FRAME_WIDTH))
        self._surf_monster.fill(BG_COLOR1)
        self._rect_monster = self._surf_monster.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, SCREEN_HEIGHT / 2 + FRAME_WIDTH)

        self._surf_bg = pygame.Surface(SCREEN_SIZE)
        self._surf_bg.fill(FRAME_COLOR)

        self._font = pygame.font.Font('./res/PingFang.ttc', 20)

    def main_loop(self):
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            clock.tick(120)
            self._screen.blit(self._surf_bg, (0, 0))
            self._screen.blit(self._surf_main, self._rect_main)
            self._screen.blit(self._surf_input, self._rect_input)
            self._screen.blit(self._surf_role, self._rect_role)
            self._screen.blit(self._surf_monster, self._rect_monster)

            text_obj = self._font.render('年轻的白龙', True, (255, 255, 255))
            self._screen.blit(text_obj, (600, 320))

            pygame.display.flip()

        pygame.quit()
