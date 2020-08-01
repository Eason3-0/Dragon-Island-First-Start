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

    pg.mixer.music.load(MUSIC['overworld'])  # Background music
    pg.mixer.music.play(-1, 0.0)
    mute = True
    pg.mixer.music.set_volume(0.0)

    active_scene = Mainmenu_Scene()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_m:
                    mute = not mute
                    volume_level = 0.0 if mute else 1.0
                    pg.mixer.music.set_volume(volume_level)
                else:
                    active_scene.process_input(event)
            elif event.type in [MOUSEMOTION, MOUSEBUTTONDOWN]:
                active_scene.process_input(event)
            elif event.type == QUIT:
                running = False

        active_scene.update()
        active_scene.render()

        # change active_scene to its next and reset its next to itself
        active_scene.next, active_scene = active_scene, active_scene.next

        fps_clock.tick(FPS)
        pg.display.update()

    quit_game()
