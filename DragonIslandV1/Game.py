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

        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.surf_main = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT * 2 / 3))
        self.surf_main.fill(BG_COLOR1)
        self.rect_main = self.surf_main.get_rect()

        self.surf_input = pygame.Surface((SCREEN_WIDTH * 2 / 3, SCREEN_HEIGHT / 3 - FRAME_WIDTH))
        self.surf_input.fill(BG_COLOR1)
        self.rect_input = self.surf_input.get_rect().move(0, SCREEN_HEIGHT * 2 / 3 + FRAME_WIDTH)

        self.surf_role = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2))
        self.surf_role.fill(BG_COLOR1)
        self.rect_role = self.surf_role.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, 0)

        self.surf_monster = pygame.Surface((SCREEN_WIDTH / 3 - FRAME_WIDTH, SCREEN_HEIGHT / 2 - FRAME_WIDTH))
        self.surf_monster.fill(BG_COLOR1)
        self.rect_monster = self.surf_monster.get_rect().move(SCREEN_WIDTH * 2 / 3 + FRAME_WIDTH, SCREEN_HEIGHT / 2 + FRAME_WIDTH)

        self.surf_bg = pygame.Surface(SCREEN_SIZE)
        self.surf_bg.fill(FRAME_COLOR)

        self._font = pygame.font.Font('./res/FZXIANGSU16.TTF', 16)

    def update_creature_info(self, creature, surf):
        y = 10
        surf.fill(BG_COLOR1)
        status_str = creature.get_status_str()
        status_text_list = status_str.split(',')
        
        text_obj = self._font.render(f'职业: {creature.Name}', False, TEXT_COLOR)
        surf.blit(text_obj, (10, 5))z
        
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

            self.update_creature_info(role, self.surf_role)
            self.update_creature_info(monster, self.surf_monster)

            self.screen.blit(self.surf_bg, (0, 0))
            self.screen.blit(self.surf_main, self.rect_main)
            self.screen.blit(self.surf_input, self.rect_input)
            self.screen.blit(self.surf_role, self.rect_role)
            self.screen.blit(self.surf_monster, self.rect_monster)
            
        

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.main_loop()
