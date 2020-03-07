import os
import sys
import pygame as pg

def load_all_images(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics

def load_files(directory, accept=('')):
    files = {}
    for f in os.listdir(directory):
        name, ext = os.path.splitext(f)
        if ext.lower() in accept:
            files[name] = os.path.join(directory, f)
    return files

def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    return load_files(directory, accept)

def load_all_fonts(directory, accept=('.ttf')):
    return load_files(directory, accept)

def load_all_tmx(directory, accept=('.tmx')):
    return load_files(directory, accept)

def load_all_sfx(directory, accept=('.wav','.mp3','.ogg','.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

def get_image(x, y, width, height, sprite_sheet):
    """Extracts image from sprite sheet"""
    image = pg.Surface([width, height])
    rect = image.get_rect()

    image.blit(sprite_sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(c.BLACK)

    return image

def get_tile(x, y, tileset, width=16, height=16, scale=1):
    """Gets the surface and rect for a tile"""
    surface = get_image(x, y, width, height, tileset)
    surface = pg.transform.scale(surface, (int(width*scale), int(height*scale)))
    rect = surface.get_rect()

    tile_dict = {'surface': surface,
                 'rect': rect}

    return tile_dict

def quit_game():
    pg.quit()
    sys.exit()