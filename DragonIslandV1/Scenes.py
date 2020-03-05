# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from settings import *
from tools import *


def tile_to_pixel(tile_x, tile_y, adj_x=0, adj_y=0):
    return (tile_x * 40 + adj_x, tile_y * 40 + adj_y)


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


def render_menuitem_centered(text, tile_x, tile_y, width:int, adj_x=0, adj_y=0):
    if width < 3:
        raise ValueError('width cannot less than 3')

    set_tile(tile_x - width / 2, tile_y, 'styled_button_left')
    for i in range(1, width):
        set_tile(tile_x - width / 2 + i, tile_y, 'button_middle_green')

    set_tile(tile_x + width / 2, tile_y, 'styled_button_right')
    render_text_centered(text, FONT_NORMAL, WHITE, tile_x, tile_y)


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
    def ProcessInput(self, events):
        # Recieves all events that have happened
        pass

    def Update(self):
        # Game logic goes here
        pass

    @abstractmethod
    def Render(self, surf):
        # Render to the main display
        pass


class Mainmenu_Scene(SceneBase):
    def __init__(self):
        super(SceneBase, self).__init__()

    def ProcessInput(self):
        pressed = pygame.mouse.get_pressed()

    def Render(self):
        SCREEN.fill(BG_COLOR1)
        render_text_centered('DRAGON ISLAND', FONT_LARGE, LIGHTGREEN, 9.5, 2)

        render_menuitem_centered('新游戏', 9.5, 6, 5)
        render_menuitem_centered('读取存档', 9.5, 8, 5)
        render_menuitem_centered('关于', 9.5, 10, 5)
        render_menuitem_centered('退出', 9.5, 12, 5)

        #render_text_centered("按 'M' 键切换静音", FONT_NORMAL, WHITE, 9.5, 13)


class CharactorSelection_Scene(SceneBase):
    pass


class Shop_Scene(SceneBase):
    pass
