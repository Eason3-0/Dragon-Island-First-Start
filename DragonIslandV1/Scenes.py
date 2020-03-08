# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import time
import sys

from settings import *
from tools import *
from textrect import render_textrect
from Creatures import *

from pygame.locals import *
import pygame as pg

MAIN_MENU = None  # Stored global main menu instance

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
    def __init__(self, text, tile_left, tile_right, tile_y, menu_type, parent_scene, action=None):
        # menu_type: 0 means null menu; 1 means normal menu; 2 means arrow menu
        self.text = text
        self.tile_left = tile_left
        self.tile_right = tile_right
        self.tile_y = tile_y
        self.menu_type = menu_type
        self.parent_scene = parent_scene
        self.action_on_clicked = action

    def on_clicked(self):
        # execute the function assigned by parent scene
        if self.action_on_clicked:
            self.action_on_clicked()
        else:  # if menuitem has not related to any action, show a hint
            self.parent_scene.next = Message_Scene('Not implemented', self.parent_scene)

    def mouse_in_me(self):
        # Tests if the mouse is anywhere between any of the
        return mouse_between_tiles(self.tile_left, self.tile_y, self.tile_right, self.tile_y)

    def render(self, been_selected=False, override_menu_type=-1):
        text_color = YELLOW if been_selected else WHITE
        text_font = FONT_NORMAL2 if been_selected else FONT_NORMAL
        cur_menu_type = override_menu_type if override_menu_type >= 0 else self.menu_type

        if cur_menu_type > 0:
            if cur_menu_type == 2:
                left_image = 'end_button_left_green'
                middle_image = 'button_middle_green'
                right_image = 'arrow_button_right'
            else:  # 1 
                left_image = 'styled_button_left'
                middle_image = 'button_middle_green'
                right_image = 'styled_button_right'
            
            set_tile(self.tile_left, self.tile_y, left_image)
            set_tile(self.tile_right, self.tile_y, right_image)

            for tile_x in range(self.tile_left + 1, self.tile_right):
                set_tile(tile_x, self.tile_y, middle_image)

        tile_x = (self.tile_left + self.tile_right) / 2
        render_text_centered(self.text, text_font, text_color, tile_x, self.tile_y)


class SceneBase(ABC):
    @property
    def selected_index(self):
        return self._selected_index
    
    @selected_index.setter
    def selected_index(self, value):
        value %= len(self.menuitems)
        if self._selected_index != value:
            self._selected_index = value
            SFX['thud'].play()

    def __init__(self):
        self.next = self
        self.menuitems = []
        self._selected_index = 0

    def process_input(self, event):
        # Recieves all events that have happened
        menuitem_clicked = None
        if event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_RETURN]:  # 键盘输入
                if event.key in [K_UP, K_DOWN] and len(self.menuitems) > 1:
                    self.selected_index += (1 if event.key == K_DOWN else -1)
                elif event.key == K_RETURN:
                    menuitem_clicked = self.menuitems[self.selected_index]
        elif event.type == MOUSEBUTTONDOWN:  # 鼠标点击
            for index, item in enumerate(self.menuitems):
                if item.mouse_in_me():
                    self.selected_index = index
                    menuitem_clicked = item
                    break
        elif event.type == MOUSEMOTION:  # Mouse hover
            for index, item in enumerate(self.menuitems):
                if item.mouse_in_me() and self.selected_index != index:
                    self.selected_index = index
                    break

        if menuitem_clicked:
            menuitem_clicked.on_clicked()

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
        global MAIN_MENU
        MAIN_MENU = self

        def new_game_action(): self.next = CharactorSelection_Scene()

        def about_action():
            message_lines = ('~~~~欢迎到来~~~~\n'
                            'DRAGON ISLAND: FIRST START\n'
                            '本游戏由\nHACKER.C.D. GAME STUDIO\n'
                            '开发制作.\n游戏愉快 ；）')
            self.next = Message_Scene(message_lines, self)

        self.menuitems = (Menuitem('新 游 戏', 7, 12, 6, 1, self, new_game_action),
                          Menuitem('读 取 存 档', 7, 12, 8, 1, self),
                          Menuitem('关 于', 7, 12, 10, 1, self, about_action),
                          Menuitem('退 出', 7, 12, 12, 1, self, quit_game))

    def render(self):
        SCREEN.fill(BG_COLOR1)

        render_text_centered('DRAGON ISLAND', FONT_LARGE, LIGHTGREEN, 9.5, 1.8)
        render_text_centered('FIRST START', FONT_LARGE, LIGHTGREEN, 9.5, 3)

        for index, item in enumerate(self.menuitems):
            item.render(index == self.selected_index)
        #render_text_centered("按 'M' 键切换静音", FONT_NORMAL, WHITE, 9.5, 13)


class CharactorSelection_Scene(SceneBase):
    def __init__(self):
        super().__init__()

        self.dic_roles = {0: Role_Fighter(),
                          1: Role_Wizard(),
                          2: Role_Ranger()}
        self.role_index = 0

        def back_action(): self.next = MAIN_MENU
        self.menuitems = (#Menuitem('说 明', 1, 4, 2.5, 1, self, func_intro),
                          Menuitem('战 士' + ' ' * 8, 1, 6, 4, 0, self),
                          Menuitem('法 师' + ' ' * 8, 1, 6, 7.5, 0, self),
                          Menuitem('游 侠' + ' ' * 8, 1, 6, 11, 0, self),
                          Menuitem('返 回', 1, 4, 13, 1, self, back_action),)

    def update(self):
        # if selected a role
        if self.selected_index < len(self.dic_roles):
            self.role_index = self.selected_index

    def render(self):
        # Render to the main display
        SCREEN.fill(BG_COLOR1)

        for i in range(15):
            set_tile(6, i, 'vertical_divider')

        rect = pg.Rect(15, 20, 200, 300)
        surf = render_textrect('请从列表\n中选择你\n喜欢的职业', FONT_SMALL, rect, WHITE, 1, 1.5)
        SCREEN.blit(surf, rect)

        for index, item in enumerate(self.menuitems):
            is_selected = index == self.selected_index
            menu_type = 2 if index == self.role_index else -1
            item.render(is_selected, menu_type)

        role = self.dic_roles.get(self.role_index)
        if role:
            rect = pg.Rect(400, 50, 400, 240)
            surf = render_textrect(role.Name, FONT_NORMAL3, rect, WHITE, 0, 1.4)
            SCREEN.blit(surf, rect)

            text = role.get_status_str()
            rect = pg.Rect(400, 100, 400, 240)
            surf = render_textrect(text, FONT_NORMAL, rect, WHITE, 0, 1.4)
            SCREEN.blit(surf, rect)

            image = IMAGES[role.sprite_name]
            SCREEN.blit(image, (500, 50))

        message = ('我们的世界由五大属性组成，分别是：\n'
                   '防御值（AC）：在你遭受攻击时挡住攻击\n'
                   '生命值（HP）：在你受到攻击时遭受的伤害\n'
                   '攻击加值（AB）：在你挥出巨剑时带给敌方的痛苦感受\n'
                   '灵敏值（QB）：在你躲过敌方致命一击时的冲刺\n'
                   '金钱（Money）：你胜利击退可恶的铁脑壳时获取的奖赏\n'
                   '除Money之外, 任何一项为0，你都会死亡')
        
        rect = pg.Rect(300, 360, 440, 240)
        surf = render_textrect(message, FONT_SMALL, rect, (200, 200, 200), 0, 1.5)
        SCREEN.blit(surf, rect)

class Shop_Scene(SceneBase):
    pass


class Message_Scene(SceneBase):
    def __init__(self, msg, scene_from):
        super().__init__()
        self.message = msg
        self.scene_from = scene_from

        def func_back(): self.next = scene_from
        menuitem_back = Menuitem('返 回', 8, 11, 2, 1, self, func_back)
        self.menuitems = (menuitem_back,)

    def render(self):
        # Render to the main display
        SCREEN.fill(BG_COLOR1)
        rect = pg.Rect(100, 200, 600, 500)
        surf = render_textrect(self.message, FONT_NORMAL, rect, WHITE, 1)
        SCREEN.blit(surf, rect)

        for index, item in enumerate(self.menuitems):
            item.render(index == self.selected_index)
