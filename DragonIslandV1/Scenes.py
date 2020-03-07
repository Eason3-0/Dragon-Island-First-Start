# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import time
import sys

from settings import *
from tools import *
from textrect import render_textrect

from pygame.locals import *
import pygame as pg


def tile_to_pixel(tile_x, tile_y, adj_x=0, adj_y=0):
    return (tile_x * 40 + adj_x, tile_y * 40 + adj_y)


def pixel_to_tile(x, y):
    return (x / 40, y / 40)


def render_text_centered(text, font, color, tile_x, tile_y):
    # Renders text centered on the given tile co-ordinate
    text_surf = font.render(text, False, color)
    text_rect = text_surf.get_rect()
    text_rect.center = tile_to_pixel(tile_x, tile_y, 20, 20)
    SCREEN.blit(text_surf, text_rect)


def set_tile(tile_x, tile_y, tile_name):
    # Sets the tile at (x, y) to the designated image
    image = TILES[tile_name]
    SCREEN.blit(image, tile_to_pixel(tile_x, tile_y))


def mouse_between_tiles(x1, y1, x2, y2):
    # Tests if the mouse is anywhere between any of the
    mouse_x, mouse_y = pg.mouse.get_pos()
    top_left = tile_to_pixel(x1, y1)
    bottom_right = tile_to_pixel(x2, y2, 39, 39)
    if mouse_x >= top_left[0] and mouse_x <= bottom_right[0] \
       and mouse_y >= top_left[1] and mouse_y <= bottom_right[1]:
        return True


class Menuitem(object):
    def __init__(self, text, tile_left, tile_right, tile_y, menu_type, func=None):
        # menu_type: 0 means normal menu; 1 means arrow menu
        self.text = text
        self.tile_left = tile_left
        self.tile_right = tile_right
        self.tile_y = tile_y
        self.menu_type = menu_type
        self.font = FONT_NORMAL
        self.func = func

    def execute(self, parent_scene):
        # execute the function assigned by parent scene
        if self.func:
            self.func(parent_scene)
        else:
            parent_scene.next = Message_Scence('Not implemented', parent_scene)

    def mouse_in_me(self):
        # Tests if the mouse is anywhere between any of the
        return mouse_between_tiles(self.tile_left, self.tile_y, self.tile_right, self.tile_y)

    def render(self, been_selected=False):
        text_color = YELLOW if been_selected else WHITE
        left_image = 'styled_button_left'
        middle_image = 'button_middle_green'
        right_image = 'styled_button_right'

        set_tile(self.tile_left, self.tile_y, left_image)
        set_tile(self.tile_right, self.tile_y, right_image)

        for tile_x in range(self.tile_left + 1, self.tile_right):
            set_tile(tile_x, self.tile_y, middle_image)

        tile_x = (self.tile_left + self.tile_right) / 2
        render_text_centered(self.text, self.font, text_color, tile_x, self.tile_y)


class SceneBase(ABC):
    def __init__(self):
        self.next = self

    @abstractmethod
    def process_input(self, key=None):
        # Recieves all events that have happened
        pass

    def update(self):
        # Game logic goes here
        pass

    @abstractmethod
    def render(self):
        # Render to the main display
        pass


class Mainmenu_Scene(SceneBase):
    def __init__(self):
        super().__init__()

        func_exit = lambda scene: quit_game()
        def func_about(scene):
            message_lines = ('~~~~欢迎到来~~~~\n'
                            'DRAGON ISLAND: FIRST START\n'
                            '本游戏由\nHACKER.C.D. GAME STUDIO\n'
                            '开发制作.\n游戏愉快 ；）')
            self.next = Message_Scence(message_lines, self)

        self.menuitems = (Menuitem('新 游 戏', 7, 12, 6, 0),
                          Menuitem('读 取 存 档', 7, 12, 8, 0),
                          Menuitem('关 于', 7, 12, 10, 0, func_about),
                          Menuitem('退 出', 7, 12, 12, 0, func_exit))
        self.selected_index = 0

    def process_input(self, key=None):
        menuitem_clicked = None
        if key:  # 键盘输入
            if key in [K_UP, K_DOWN]:
                SFX['thud'].play()
                self.selected_index += (1 if key == K_DOWN else -1)
                self.selected_index %= len(self.menuitems) # keep in 0 ~ menuitem count
            elif key == K_RETURN:
                menuitem_clicked = self.menuitems[self.selected_index]
        else:  # 鼠标点击
            if pg.mouse.get_pressed()[0]:
                for index, item in enumerate(self.menuitems):
                    if item.mouse_in_me():
                        self.selected_index = index
                        menuitem_clicked = self.menuitems[self.selected_index]
                        break

        if menuitem_clicked:
            menuitem_clicked.execute(self)

    def render(self):
        SCREEN.fill(BG_COLOR1)
        render_text_centered('DRAGON ISLAND', FONT_LARGE, LIGHTGREEN, 9.5, 1.8)
        render_text_centered('FIRST START', FONT_LARGE, LIGHTGREEN, 9.5, 3)
        for index, item in enumerate(self.menuitems):
            item.render(index == self.selected_index)

        #render_text_centered("按 'M' 键切换静音", FONT_NORMAL, WHITE, 9.5, 13)


class CharactorSelection_Scene(SceneBase):
    pass


class Shop_Scene(SceneBase):
    pass


class Message_Scence(SceneBase):
    def __init__(self, msg, scene_from):
        super().__init__()
        def func_back(scene):
            scene.scene_from.next = scene.scene_from
            scene.next = scene.scene_from

        self.menuitem_back = Menuitem('返 回', 8, 11, 2, 0, func_back)
        self.message = msg
        self.scene_from = scene_from

    def process_input(self, key=None):
        # Recieves all events that have happened
        menuitem_clicked = None
        if key in [K_RETURN, K_ESCAPE] or pg.mouse.get_pressed()[0] and self.menuitem_back.mouse_in_me():
            menuitem_clicked = self.menuitem_back
        
        if menuitem_clicked:
            menuitem_clicked.execute(self)

    def Update(self):
        # Game logic goes here
        pass

    def render(self):
        # Render to the main display
        SCREEN.fill(BG_COLOR1)
        rect = pg.Rect(100, 200, 600, 500)
        surf = render_textrect(self.message, FONT_NORMAL, rect, WHITE, 1)
        SCREEN.blit(surf, rect)
        self.menuitem_back.render(True)
