# -*- coding:utf-8 -*-
# 图形界面版 version 0.5.0a1

import os

import pygame as pg
from pygame.locals import *

import Creatures
import tools
from settings import *
from Scenes import *

class Game(object):

    def __init__(self):
        self.surf_bg = pg.Surface(SCREEN_SIZE)
        self.surf_bg.fill(BG_COLOR1)

    def update_creature_info(self, creature, surf):
        y = 10
        surf.fill(BG_COLOR1)
        status_str = creature.get_status_str()
        status_text_list = status_str.split(',')
        
        text_obj = FONT.render(f'职业: {creature.Name}', False, TEXT_COLOR)
        surf.blit(text_obj, (10, 5))
        
        y += text_obj.get_rect().height * 1.5
        for status_text in status_text_list:
            text_obj = FONT.render(status_text.lstrip(), False, TEXT_COLOR)
            surf.blit(text_obj, (10, y))
            y += text_obj.get_rect().height * 1.5

    def main_loop(self):
        fps_clock = pg.time.Clock()
        role = Creatures.Role_Fighter()
        monster = Creatures.Monster_GoblinCutter()

        # Background music
        background_music = pg.mixer.music.load(MUSIC['overworld'])
        pg.mixer.music.play(-1, 0.0)
        mute = False

        active_scene = Mainmenu_Scene()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_m:
                        if mute == False:
                            pg.mixer.music.set_volume(0.0)
                            mute = True
                        elif mute == True:
                            pg.mixer.music.set_volume(1.0)
                            mute = False
                elif event.type == QUIT:
                    running = False

            active_scene.Render()

            fps_clock.tick(FPS)

            # self.update_creature_info(role, self.surf_role)
            # self.update_creature_info(monster, self.surf_monster)

            #SCREEN.blit(self.surf_bg, (0, 0))

            pg.display.flip()

        pg.quit()

if __name__ == "__main__":
    game = Game()
    game.main_loop()
