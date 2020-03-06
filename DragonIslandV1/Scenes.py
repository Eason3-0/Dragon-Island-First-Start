# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import time
import sys

from settings import *
from tools import *

from pygame.locals import *
import pygame as pg


def tile_to_pixel(tile_x, tile_y, adj_x=0, adj_y=0):
    return (tile_x * 40 + adj_x, tile_y * 40 + adj_y)


def pixel_to_tile(x, y):
    return (x / 40 , y / 40)


def render_text_centered(text, font, color, tile_x, tile_y):
    # Renders text centered on the given tile co-ordinate
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = tile_to_pixel(tile_x, tile_y, 20, 20)
    SCREEN.blit(text_surf, text_rect)


def set_tile(tile_x, tile_y, tile_name):
    # Sets the tile at (x, y) to the designated image
    image = TILES[tile_name]
    SCREEN.blit(image, tile_to_pixel(tile_x, tile_y))


def render_menuitem_centered(text,  tile_x, tile_y, width:int, is_selected, adj_x=0, adj_y=0):
    if width < 3:
        raise ValueError('width cannot less than 3')
    
    if is_selected:
        color = YELLOW
    else:
        color = WHITE

    set_tile(tile_x - width / 2, tile_y, 'styled_button_left')
    for i in range(1, width):
        set_tile(tile_x - width / 2 + i, tile_y, 'button_middle_green')

    set_tile(tile_x + width / 2, tile_y, 'styled_button_right')
    render_text_centered(text, FONT_NORMAL, color, tile_x, tile_y)


def mouse_between_tiles(x1, y1, x2, y2):
    # Tests if the mouse is anywhere between any of the
    mouse_x, mouse_y = pygame.mouse.get_pos()
    top_left = tile_to_pixel(x1, y1)
    bottom_right = tile_to_pixel(x2 + 1, y2 + 1)
    if mouse_x >= top_left[0] and mouse_x < bottom_right[0] \
       and mouse_y >= top_left[1] and mouse_y < bottom_right[1]:
        return True


class SceneBase(ABC):
    def __init__(self):
        self.next = self

    @abstractmethod
    def ProcessInput(self, key=None):
        # Recieves all events that have happened
        pass

    def Update(self):
        # Game logic goes here
        pass

    @abstractmethod
    def Render(self):
        # Render to the main display
        pass


class Mainmenu_Scene(SceneBase):
    def __init__(self):
        super().__init__()

        self.menu_items = ['新 游 戏', '读 取 存 档', '关 于', '退 出']
        self.selected_menuitem_index = 0
        
        self.NEW_GAME_INDEX = 0
        self.LOAD_GAME_INDEX = 1
        self.ABOUT_INDEX = 2
        self.EXIT_INDEX = 3


    def ProcessInput(self, key=None):
        do_enter = False
        if key:            
            if key in [K_UP, K_DOWN]:
                SFX['thud'].play()
                if key == K_UP:
                    self.selected_menuitem_index -= 1
                else:
                    self.selected_menuitem_index += 1
            elif key == K_RETURN:
                do_enter = True
            else:
                return

            self.selected_menuitem_index %= len(self.menu_items)
        else:
            pressed = pg.mouse.get_pressed()
            if pressed[0]:            
                index = self.get_mouse_menuitem()
                if index >= 0:
                    self.selected_menuitem_index = index
                    do_enter = True
        
        if do_enter:
            if self.selected_menuitem_index == self.EXIT_INDEX:
                pg.quit()
                sys.exit()
            else:
                self.next = Message_Scence('Not implemented')

    def Render(self):
        SCREEN.fill(BG_COLOR1)
        render_text_centered('DRAGON ISLAND', FONT_LARGE, LIGHTGREEN, 9.5, 2)

        tile_y = 6
        distance = 2

        for index, item in enumerate(self.menu_items):
            render_menuitem_centered(item, 9.5, tile_y, 5, index == self.selected_menuitem_index)
            tile_y += distance

        #render_text_centered("按 'M' 键切换静音", FONT_NORMAL, WHITE, 9.5, 13)

    def get_mouse_menuitem(self):
        # Tests if the mouse is anywhere between any of the
        mousex, mousey = pg.mouse.get_pos()
        tile_x, tile_y = pixel_to_tile(mousex, mousey)
        
        if 7 < tile_x < 12:
            tile_y -= 6
            if 0 < tile_y < 1:
                return 0
            elif 2 < tile_y < 3:
                return 1
            elif 4 < tile_y < 5:
                return 2
            elif 6 < tile_y < 7:
                return 3
            else:
                return -1
        else:
            return -1
            

class CharactorSelection_Scene(SceneBase):
    pass


class Shop_Scene(SceneBase):
    pass

class Message_Scence(SceneBase):
    def __init__(self, msg):
        super().__init__()
        self.message = msg
        self.parent_scene = Mainmenu_Scene()
    
    def ProcessInput(self, key=None):
        # Recieves all events that have happened
        if key == K_RETURN:
            self.next = self.parent_scene

    def Update(self):
        # Game logic goes here
        pass
    
    def Render(self):
        # Render to the main display
        SCREEN.fill(BG_COLOR1)
        render_text_centered(self.message, FONT_NORMAL, WHITE, 9.5, 7)
        