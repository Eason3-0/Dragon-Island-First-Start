# -*- coding:utf-8 -*-
# 图形界面版 version 0.5.0a1

import os

import pygame as pg
from pygame.locals import *

import Creatures
import tools
from settings import *
from Scenes import *

if __name__ == '__main__':
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
                else:
                    active_scene.process_input(event.key)
            elif event.type == QUIT:
                running = False

        active_scene.process_input()
        active_scene.update()
        active_scene.render()
        active_scene = active_scene.next

        fps_clock.tick(FPS)

        pg.display.flip()

    quit_game()