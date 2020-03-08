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

    # Background music
    background_music = pg.mixer.music.load(MUSIC['overworld'])
    pg.mixer.music.play(-1, 0.0)
    mute = False

    active_scene = Mainmenu_Scene()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_m:
                    if mute == False:
                        pg.mixer.music.set_volume(0.0)
                        mute = True
                    elif mute == True:
                        pg.mixer.music.set_volume(1.0)
                        mute = Fals
                else:
                    active_scene.process_input(event)
            elif event.type in [MOUSEMOTION, MOUSEBUTTONDOWN]:
                active_scene.process_input(event)
            elif event.type == QUIT:
                running = False

        active_scene.update()
        active_scene.render()

        # change active_scene to its next and reset its next to itself
        old_scene = active_scene
        active_scene = active_scene.next
        old_scene.next = old_scene

        fps_clock.tick(FPS)
        pg.display.flip()

    quit_game()
