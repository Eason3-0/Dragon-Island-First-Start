import os
import pygame as pg
import tools

# Colour      R    G    B   (A)
# ==============================
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)
YELLOW = (255, 255, 0)
LIGHTGREEN = (137, 199, 94)

FRAME_COLOR = (60, 60, 60)
BG_COLOR1 = (0, 0, 0)
BG_COLOR2 = (220, 220, 220)
TEXT_COLOR = (255, 255, 255)

TILE_SIZE = 40
HALF_TILE_SIZE = 20

FPS = 30

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FRAME_WIDTH = 3

# 设置运行环境
work_dir = os.path.split(os.path.abspath(__file__))[0]
os.chdir(work_dir)  # 切换工作目录到当前文件目录，方便加载资源
os.environ['SDL_VIDEO_CENTERED'] = '1'  # 使Pygame窗体居中

# Pygame窗口初始化
pg.init()
SCREEN = pg.display.set_mode(SCREEN_SIZE)

FONTS = tools.load_all_fonts(os.path.join('resources', 'fonts'))
MUSIC = tools.load_all_music(os.path.join('resources', 'music'))
IMAGES = tools.load_all_images(os.path.join('resources', 'images'))
TILES = tools.load_all_images(os.path.join('resources', 'tiles'))
SFX = tools.load_all_sfx(os.path.join('resources', 'sound'))
# TMX = tools.load_all_tmx(os.path.join('resources', 'tmx'))

pg.display.set_caption('Dragon Island 1.0')
pg.display.set_icon(IMAGES['icon'])

FONT_NORMAL = pg.font.Font(FONTS['FZXIANGSU'], 20)
FONT_LARGE = pg.font.Font(FONTS['FZXIANGSU12'], 36)
FONT_LARGE.set_bold(True)
