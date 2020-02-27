# -*- coding:utf-8 -*-
# 图形界面版 version 0.5.0a1

import os

import pygame
from pygame.locals import *

import Creatures

# Constants
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FRAME_WIDTH = 3

FRAME_COLOR = (60, 60, 60)
BG_COLOR1 = (0, 0, 0)
BG_COLOR2 = (220, 220, 220)
TEXT_COLOR = (255, 255, 255)

MUSIC = './res/overworld.mp3'
FPS = 30

class Game(object):

    def __init__(self):
        # 设置运行环境
        work_dir = os.path.split(os.path.abspath(__file__))[0]
        os.chdir(work_dir)  # 切换工作目录到当前文件目录，方便加载资源
        os.environ['SDL_VIDEO_CENTERED'] = '1'  # 使Pygame窗体居中

        # Pygame窗口初始化
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

        self._font = pygame.font.Font('./res/FZXIANGSU16.TTF', 16)

    def update_creature_info(self, creature, surf):
        y = 10
        surf.fill(BG_COLOR1)
        status_str = creature.get_status_str()
        status_text_list = status_str.split(',')
        
        text_obj = self._font.render(f'职业: {creature.Name}', False, TEXT_COLOR)
        surf.blit(text_obj, (10, 5))
        
        y += text_obj.get_rect().height * 1.5
        for status_text in status_text_list:
            text_obj = self._font.render(status_text.lstrip(), False, TEXT_COLOR)
            surf.blit(text_obj, (10, y))
            y += text_obj.get_rect().height * 1.5

    def main_loop(self):
        fps_clock = pygame.time.Clock()
        role = Creatures.Role_Fighter()
        monster = Creatures.Monster_GoblinCutter()

        # Background music
        background_music = pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.play(-1, 0.0)
        mute = False

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_m:
                        if mute == False:
                            pygame.mixer.music.set_volume(0.0)
                            mute = True
                        elif mute == True:
                            pygame.mixer.music.set_volume(1.0)
                            mute = False
                elif event.type == QUIT:
                    running = False

            fps_clock.tick(FPS)

            self.update_creature_info(role, self._surf_role)
            self.update_creature_info(monster, self._surf_monster)

            self._screen.blit(self._surf_bg, (0, 0))
            self._screen.blit(self._surf_main, self._rect_main)
            self._screen.blit(self._surf_input, self._rect_input)
            self._screen.blit(self._surf_role, self._rect_role)
            self._screen.blit(self._surf_monster, self._rect_monster)
            
        

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.main_loop()
