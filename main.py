import pygame
from pygame import mixer
import os
import random
import csv
import data.button as button
#import data.pyganim as pyganim
import sys
from param import *
import time
import math
from numba import njit, prange
from save import *

mixer.init()
pygame.init()

ver='Mobile 0.0.1'

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.display.set_caption(f'                                                                                                                                                                           Shoot Arena {ver}. BY NASHDARK81')
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.flip()

clock = pygame.time.Clock()
FPS = 60

click=False

enemy_number=0

GRAVITY = 0.70
SCROLL_THRESH = 550
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 23
MAX_LEVELS = 1
screen_scroll =0
bg_scroll = 0
level = 1
score=0
mana=20

playtime=0
pig_time=400

john_ammo=8

main_menu_mode=True
settings_mode=False
level_mode=False
start_game = False
start_intro = False
skin_mode=False
shop_menu=False
training_show_text=False
training_show_controls=False

mobile_version=True

settings_game_mode=False
settings_video_mode=False
settings_sound_mode=False

moving_left = False
moving_right = False
shoot = False
reload=False

boss_fight=False

but_fx=False

screen_update=True

fadein_start=False
direction=0
alpha=255

particles = []
particles2 = []
particles3=[]
particles4=[]

save_data=Save()

try:
    lang = save_data.get('lang')
    john_skin_on=save_data.get('john_skin_on')
    fullscreen = save_data.get('fullscreen')
    music_volume = save_data.get('music_volume')
    fx_volume = save_data.get('fx_volume')
    voice_volume = save_data.get('voice_volume')
except:
    john_skin_on=1
    lang=1
    fullscreen=0
    music_volume=10
    fx_volume=10
    voice_volume=10

#buttons
logo_img=pygame.image.load('resource/common/img/text/logo.png').convert_alpha()
logo2_img=pygame.image.load('resource/common/img/text/logo2.png').convert_alpha()

lev1_img=pygame.image.load('resource/common/img/button/lev1.png').convert_alpha()
back_img=pygame.image.load('resource/common/img/button/back.png').convert_alpha()
back2_img=pygame.image.load('resource/common/img/button/back2.png').convert_alpha()

shop_rus_img=pygame.image.load('resource/common/img/text/rus/shop.png').convert_alpha()
shop_eng_img=pygame.image.load('resource/common/img/text/eng/shop.png').convert_alpha()

settings_rus_img=pygame.image.load('resource/common/img/text/rus/settings.png').convert_alpha()
settings_eng_img=pygame.image.load('resource/common/img/text/eng/settings.png').convert_alpha()

start_rus_img = pygame.image.load('resource/common/img/text/rus/play.png').convert_alpha()
start_eng_img = pygame.image.load('resource/common/img/text/eng/play.png').convert_alpha()

exitgame_rus=pygame.image.load('resource/common/img/text/rus/exit_game.png').convert_alpha()
exitgame_eng=pygame.image.load('resource/common/img/text/eng/exit_game.png').convert_alpha()

sound_rus=pygame.image.load('resource/common/img/text/rus/sound.png').convert_alpha()
sound_eng=pygame.image.load('resource/common/img/text/eng/sound.png').convert_alpha()

game_rus=pygame.image.load('resource/common/img/text/rus/game.png').convert_alpha()
game_eng=pygame.image.load('resource/common/img/text/eng/game.png').convert_alpha()

video_rus=pygame.image.load('resource/common/img/text/rus/video.png').convert_alpha()
video_eng=pygame.image.load('resource/common/img/text/eng/video.png').convert_alpha()

rus_img=pygame.image.load('resource/common/img/button/lang/rus.png').convert_alpha()
eng_img=pygame.image.load('resource/common/img/button/lang/eng.png').convert_alpha()

music_eng=pygame.image.load('resource/common/img/text/eng/music.png').convert_alpha()

fulscreen_eng_img=pygame.image.load('resource/common/img/text/eng/fullscreen.png').convert_alpha()

change_lang_rus=pygame.image.load('resource/common/img/text/rus/change_lang.png').convert_alpha()
change_lang_eng=pygame.image.load('resource/common/img/text/eng/change_lang.png').convert_alpha()

left_img=pygame.image.load('resource/common/img/button/left.png').convert_alpha()
right_img=pygame.image.load('resource/common/img/button/right.png').convert_alpha()

skin_img=pygame.image.load('resource/common/img/button/skin.png').convert_alpha()

go_r_img=pygame.image.load('resource/common/img/button/go_r.png').convert_alpha()
go_l_img=pygame.image.load('resource/common/img/button/go_l.png').convert_alpha()
jump_img=pygame.image.load('resource/common/img/button/jump.png').convert_alpha()
shoot_img=pygame.image.load('resource/common/img/button/shoot.png').convert_alpha()
reload_img=pygame.image.load('resource/common/img/button/reload.png').convert_alpha()
shift_img=pygame.image.load('resource/common/img/button/shift.png').convert_alpha()
ctrl_img=pygame.image.load('resource/common/img/button/ctrl.png').convert_alpha()

john_1_skin_on=pygame.image.load('resource/common/img/icon/skins/john/1_on.png').convert_alpha()
john_1_skin_off=pygame.image.load('resource/common/img/icon/skins/john/1_off.png').convert_alpha()
john_2_skin_on=pygame.image.load('resource/common/img/icon/skins/john/2_on.png').convert_alpha()
john_2_skin_off=pygame.image.load('resource/common/img/icon/skins/john/2_off.png').convert_alpha()
john_3_skin_on=pygame.image.load('resource/common/img/icon/skins/john/3_on.png').convert_alpha()
john_3_skin_off=pygame.image.load('resource/common/img/icon/skins/john/3_off.png').convert_alpha()
john_soon_skin=pygame.image.load('resource/common/img/icon/skins/john/soon.png').convert_alpha()

zero_img=pygame.image.load('resource/common/img/text/0.png').convert_alpha()
one_img=pygame.image.load('resource/common/img/text/1.png').convert_alpha()
two_img=pygame.image.load('resource/common/img/text/2.png').convert_alpha()
three_img=pygame.image.load('resource/common/img/text/3.png').convert_alpha()
four_img=pygame.image.load('resource/common/img/text/4.png').convert_alpha()
five_img=pygame.image.load('resource/common/img/text/5.png').convert_alpha()
six_img=pygame.image.load('resource/common/img/text/6.png').convert_alpha()
seven_img=pygame.image.load('resource/common/img/text/7.png').convert_alpha()
eight_img=pygame.image.load('resource/common/img/text/8.png').convert_alpha()
nine_img=pygame.image.load('resource/common/img/text/9.png').convert_alpha()

on_img=pygame.image.load('resource/common/img/text/on.png').convert_alpha()
off_img=pygame.image.load('resource/common/img/text/off.png').convert_alpha()
#img
shootgun_img=pygame.image.load('resource/common/img/icon/weapon/shootgun.png').convert_alpha()
score_img=pygame.image.load('resource/common/img/icon/score.png').convert_alpha()
plevok_img=pygame.image.load('resource/common/img/icon/plevok.png').convert_alpha()
closed_rus_img=pygame.image.load('resource/common/img/icon/closed_rus.png').convert_alpha()
closed_eng_img=pygame.image.load('resource/common/img/icon/closed_eng.png').convert_alpha()

#bg
black_img=pygame.image.load('resource/common/img/bg/black.png').convert_alpha()

skin_changer_bg=pygame.image.load('resource/common/img/bg/skin_bg.png').convert_alpha()

forest_0=pygame.image.load('resource/common/img/bg/forest/0.png').convert_alpha()
forest_1=pygame.image.load('resource/common/img/bg/forest/1.png').convert_alpha()
forest_2=pygame.image.load('resource/common/img/bg/forest/2.png').convert_alpha()
forest_3=pygame.image.load('resource/common/img/bg/forest/3.png').convert_alpha()
forest_4=pygame.image.load('resource/common/img/bg/forest/4.png').convert_alpha()
forest_5=pygame.image.load('resource/common/img/bg/forest/5.png').convert_alpha()

city_img=pygame.image.load('resource/common/img/bg/city/0.png').convert_alpha()

settings_img=pygame.image.load('resource/common/img/bg/settings.png').convert_alpha()
shop_bg=pygame.image.load('resource/common/img/bg/shop.png')

day_main_0_img=pygame.image.load('resource/common/img/bg/main_menu/day/0.png').convert_alpha()
day_main_1_img=pygame.image.load('resource/common/img/bg/main_menu/day/1.png').convert_alpha()
day_main_2_img=pygame.image.load('resource/common/img/bg/main_menu/day/2.png').convert_alpha()

#ammo
shootgun_ammo8_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_8.png').convert_alpha()
shootgun_ammo7_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_7.png').convert_alpha()
shootgun_ammo6_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_6.png').convert_alpha()
shootgun_ammo5_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_5.png').convert_alpha()
shootgun_ammo4_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_4.png').convert_alpha()
shootgun_ammo3_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_3.png').convert_alpha()
shootgun_ammo2_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_2.png').convert_alpha()
shootgun_ammo1_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_1.png').convert_alpha()
shootgun_ammo0_img=pygame.image.load('resource/common/img/john/ammo/shootgun_ammo_0.png').convert_alpha()

img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'resource/common/img/Tile/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

#icon
bullet_img = pygame.image.load('resource/common/img/icon/bullet.png').convert_alpha()

#music
music = pygame.mixer.music.load('resource/common/sound/music/main.mp3')
music = pygame.mixer.music.play(-1, 0.0, 5000)

music = pygame.mixer.music.set_volume(music_volume / 10)

#fx
button_fx = pygame.mixer.Sound('resource/common/sound/fx/click.mp3')
button_fx.set_volume(fx_volume/10)
shoot_fx=pygame.mixer.Sound('resource/common/sound/fx/shoot.mp3')
shoot_fx.set_volume(fx_volume/10)
throw_fx=pygame.mixer.Sound('resource/common/sound/fx/throw.mp3')
throw_fx.set_volume(fx_volume/10)
plevok_fx=pygame.mixer.Sound('resource/common/sound/fx/plevok.mp3')
plevok_fx.set_volume(fx_volume/10)
shoot_shootgun_fx=pygame.mixer.Sound('resource/common/sound/fx/shoot_shootgun.mp3')
shoot_shootgun_fx.set_volume(fx_volume/10)
built_fx=pygame.mixer.Sound('resource/common/sound/fx/build.mp3')
built_fx.set_volume(fx_volume/10)
reload_shootgun_fx=pygame.mixer.Sound('resource/common/sound/fx/reload_shootgun.mp3')
reload_shootgun_fx.set_volume(fx_volume/10)
empty_fx=pygame.mixer.Sound('resource/common/sound/fx/empty.mp3')
empty_fx.set_volume(fx_volume/10)
choose_1_fx=pygame.mixer.Sound('resource/common/sound/fx/choose1.wav')
choose_1_fx.set_volume(fx_volume/10)
choose_2_fx=pygame.mixer.Sound('resource/common/sound/fx/choose2.wav')
choose_2_fx.set_volume(fx_volume/10)
pig_theme = pygame.mixer.Sound('resource/common/sound/music/pig_theme.mp3')
pig_theme.set_volume(music_volume/10)

#voice
ti_she_voice=pygame.mixer.Sound('resource/common/sound/voice/ти ще.wav')
ti_she_voice.set_volume(fx_volume/10)
braah_voice=pygame.mixer.Sound('resource/common/sound/voice/bwaaah.wav')
braah_voice.set_volume(fx_volume/10)
braah_voice2=pygame.mixer.Sound('resource/common/sound/voice/bwaah_reverse.mp3')
braah_voice2.set_volume(fx_volume/10)
lox_voice=pygame.mixer.Sound('resource/common/sound/voice/лох.wav')
lox_voice.set_volume(fx_volume/10)
easy_voice=pygame.mixer.Sound('resource/common/sound/voice/для кого.wav')
easy_voice.set_volume(fx_volume/10)
wtf_voice=pygame.mixer.Sound('resource/common/sound/voice/wtf.mp3')
wtf_voice.set_volume(fx_volume/10)
terrorist_win_voice=pygame.mixer.Sound('resource/common/sound/voice/terrorist_win.mp3')
terrorist_win_voice.set_volume(fx_volume/10)
postrelay_voice=pygame.mixer.Sound('resource/common/sound/voice/postrelay.mp3')
postrelay_voice.set_volume(fx_volume/10)
erotic_voice=pygame.mixer.Sound('resource/common/sound/voice/erotic.mp3')
erotic_voice.set_volume(fx_volume/10)

BG = (144, 201, 120)
RED = (255, 0, 0)
BLUE=(0,0,255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
HELL=(218, 94, 83)
ocean=(146, 123, 192)
BROWN=(46, 24, 0)
YELLOW=(255,255,0)

font = pygame.font.SysFont('Futura', 30)
font1 = pygame.font.Font('resource/fonts/pixel.ttf', 50)
font2 = pygame.font.Font('resource/fonts/Karma Future.otf', 25)

bg_menu1 = pygame.image.load("resource/common/img/bg/main_menu/day/0.png").convert()
bg_width1 = bg_menu1.get_width()
bg_rect1 = bg_menu1.get_rect()
scroll_bg1 = 0
tiles_bg1 = math.ceil(SCREEN_WIDTH  / bg_width1) + 1

bg_menu2 = pygame.image.load("resource/common/img/bg/main_menu/day/1.png").convert_alpha()
bg_width2 = bg_menu2.get_width()
bg_rect2 = bg_menu2.get_rect()
scroll_bg2 = 0
tiles_bg2 = math.ceil(SCREEN_WIDTH  / bg_width2) + 1

bg_menu3 = pygame.image.load("resource/common/img/bg/main_menu/day/2.png").convert_alpha()
bg_width3 = bg_menu3.get_width()
bg_rect3 = bg_menu3.get_rect()
scroll_bg3 = 0
tiles_bg3 = math.ceil(SCREEN_WIDTH  / bg_width3) + 1

save_data=Save()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    if level==1 and main_menu_mode==False:
        screen.fill(BLACK)
        width = forest_0.get_width()
        for x in prange(13):
            screen.blit(forest_0, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - forest_0.get_height() - 0))
            screen.blit(forest_1, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - forest_0.get_height() + 10))
            screen.blit(forest_2, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - forest_0.get_height() +20))
            screen.blit(forest_3, ((x * width) - bg_scroll * 0.9, SCREEN_HEIGHT - forest_0.get_height() +30))
            screen.blit(forest_4, ((x * width) - bg_scroll * 0.95, SCREEN_HEIGHT - forest_0.get_height() +40))
    if level==2 and main_menu_mode==False:
        width = 480
        screen.fill(ocean)
        for x in prange(10):
            screen.blit(city_img, ((x * width) - bg_scroll * 0.5, SCREEN_HEIGHT - city_img.get_height()))

def main_menu():
    global main_menu_mode, start_game, settings_mode, level_mode, shop_menu, boss_fight, mana, playtime, lang, fadein_start, alpha, skin_mode, run
    if main_menu_mode==True:
        draw_bg()
        if skin_but.draw(screen):
            main_menu_mode = False
            skin_mode = True
        if lang==1:
            if start_rus_button.draw(screen):
                level_mode=True
                playtime=0
                mana=20
                main_menu_mode=False
                boss_fight=False
                button_fx.play()
            if shop_rus_but.draw(screen):
                main_menu_mode=False
                shop_menu=True
                button_fx.play()
                music = pygame.mixer.music.load('resource/common/sound/music/shop.mp3')
                music = pygame.mixer.music.play(-1, 0.0, 5000)
            if settings_rus_but.draw(screen):
                button_fx.play()
                main_menu_mode=False
                settings_mode=True
            if exit_rus_but.draw(screen):
                run=False
        if lang==2:
            if start_eng_button.draw(screen):
                level_mode=True
                playtime=0
                mana=20
                main_menu_mode=False
                boss_fight=False
                button_fx.play()
            if shop_eng_but.draw(screen):
                main_menu_mode=False
                shop_menu=True
                button_fx.play()
                music = pygame.mixer.music.load('resource/common/sound/music/shop.mp3')
                music = pygame.mixer.music.play(-1, 0.0, 5000)
            if settings_eng_but.draw(screen):
                button_fx.play()
                main_menu_mode=False
                settings_mode=True
            if exit_eng_but.draw(screen):
                run=False
        screen.blit(logo_img, (SCREEN_WIDTH // 3 - 40, 5))
        screen.blit(logo2_img, (SCREEN_WIDTH // 3+120 , 85))

def settings():
    global  main_menu_mode, settings_mode, alpha, fadein_start, lang, settings_sound_mode, settings_game_mode, settings_video_mode
    if settings_mode==True:
        screen.blit(settings_img, (0,0))
        if lang==1:
            if sound_rus_but.draw(screen):
                settings_mode=False
                settings_sound_mode=True
            # if video_rus_but.draw(screen):
            #     settings_mode = False
            #     settings_video_mode = True
            if game_rus_but.draw(screen):
                settings_mode = False
                settings_game_mode = True
        if lang==2:
            if sound_eng_but.draw(screen):
                settings_mode = False
                settings_sound_mode = True
            # if video_eng_but.draw(screen):
            #     settings_mode = False
            #     settings_video_mode = True
            if game_eng_but.draw(screen):
                settings_mode = False
                settings_game_mode = True
        if back_but.draw(screen):
            settings_mode=False
            main_menu_mode=True
        draw_text(f'{ver} by NashDark81', font2, BLACK, 5, 680)

def settings_game():
    global lang, settings_mode, settings_game_mode, lang
    if settings_game_mode==True:
        screen.blit(settings_img, (0,0))
        if lang==1:
            screen.blit(change_lang_rus, (5, 200))
            if rus_but.draw(screen):
                pass
            if left_but.draw(screen):
                lang=2
                choose_1_fx.play()
            if right_but.draw(screen):
                lang=2
                choose_1_fx.play()
        if lang==2:
            screen.blit(change_lang_eng, (5, 190))
            if eng_but.draw(screen):
                pass
            if left_but.draw(screen):
                lang=1
                choose_1_fx.play()
            if right_but.draw(screen):
                lang=1
                choose_1_fx.play()
        if back_but.draw(screen):
            settings_mode=True
            settings_game_mode=False
        draw_text(ver, font2, BLACK, 5, 770)

def settings_video():
    global fullscreen, settings_mode, settings_video_mode, screen_update
    if settings_video_mode==True:
        screen.blit(settings_img, (0,0))
        screen.blit(fulscreen_eng_img, (430, 200))
        if fullscreen==1:
            screen.blit(off_img, (600, 300))
        if fullscreen==0:
            screen.blit(on_img, (610, 300))
        if fullscreen==1:
            if left_video_volume_but.draw(screen):
                fullscreen = 0
                screen_update = True
                choose_1_fx.play()
            if right_video_volume_but.draw(screen):
                fullscreen = 0
                screen_update = True
                choose_1_fx.play()
        if fullscreen==0:
            if left_video_volume_but.draw(screen):
                fullscreen = 1
                screen_update = True
                choose_1_fx.play()
            if right_video_volume_but.draw(screen):
                fullscreen = 1
                screen_update = True
                choose_1_fx.play()
        if back_but.draw(screen):
            settings_mode=True
            settings_video_mode=False
        draw_text(ver, font2, BLACK, 5, 770)

def settings_sound():
    global settings_mode, voice_volume, fx_volume,  settings_sound_mode, music_volume, music
    if settings_sound_mode==True:

        button_fx.set_volume(fx_volume / 10)
        shoot_fx.set_volume(fx_volume / 10)
        throw_fx.set_volume(fx_volume / 10)
        plevok_fx.set_volume(fx_volume / 10)
        shoot_shootgun_fx.set_volume(fx_volume / 10)
        built_fx.set_volume(fx_volume / 10)
        reload_shootgun_fx.set_volume(fx_volume / 10)
        empty_fx.set_volume(fx_volume / 10)
        choose_1_fx.set_volume(fx_volume / 10)
        choose_2_fx.set_volume(fx_volume / 10)
        pig_theme.set_volume(music_volume / 10)

        ti_she_voice.set_volume(fx_volume / 10)
        braah_voice.set_volume(fx_volume / 10)
        braah_voice2.set_volume(fx_volume / 10)
        lox_voice.set_volume(fx_volume / 10)
        easy_voice.set_volume(fx_volume / 10)
        wtf_voice.set_volume(fx_volume / 10)
        terrorist_win_voice.set_volume(fx_volume / 10)
        postrelay_voice.set_volume(fx_volume / 10)
        erotic_voice.set_volume(fx_volume / 10)

        music = pygame.mixer.music.set_volume(music_volume / 10)

        screen.blit(settings_img, (0,0))
        if music_eng_but.draw(screen):
            pass
        if music_volume==0:
            screen.blit(zero_img, (620, 180))
        if music_volume==1:
            screen.blit(one_img, (620, 180))
        if music_volume==2:
            screen.blit(two_img, (620, 180))
        if music_volume==3:
            screen.blit(three_img, (620, 180))
        if music_volume==4:
            screen.blit(four_img, (620, 180))
        if music_volume==5:
            screen.blit(five_img, (620, 180))
        if music_volume==6:
            screen.blit(six_img, (620, 180))
        if music_volume==7:
            screen.blit(seven_img, (620, 180))
        if music_volume==8:
            screen.blit(eight_img, (620, 180))
        if music_volume==9:
            screen.blit(nine_img, (620, 180))
        if music_volume==10:
            screen.blit(one_img, (590, 180))
            screen.blit(zero_img, (640, 180))

        if sound_eng_but.draw(screen):
            pass
        if fx_volume==0:
            screen.blit(zero_img, (620, 380))
        if fx_volume==1:
            screen.blit(one_img, (620, 380))
        if fx_volume==2:
            screen.blit(two_img, (620, 380))
        if fx_volume==3:
            screen.blit(three_img, (620, 380))
        if fx_volume==4:
            screen.blit(four_img, (620, 380))
        if fx_volume==5:
            screen.blit(five_img, (620, 380))
        if fx_volume==6:
            screen.blit(six_img, (620, 380))
        if fx_volume==7:
            screen.blit(seven_img, (620, 380))
        if fx_volume==8:
            screen.blit(eight_img, (620, 380))
        if fx_volume==9:
            screen.blit(nine_img, (620, 380))
        if fx_volume==10:
            screen.blit(one_img, (590, 380))
            screen.blit(zero_img, (640, 380))

        if back_but.draw(screen):
            settings_mode=True
            settings_sound_mode=False
            return music_volume
        if left_music_volume_but.draw(screen):
            if music_volume==0:
                pass
            if music_volume==1:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==2:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==3:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==4:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==5:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==6:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==7:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==8:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==9:
                music_volume-=1
                choose_1_fx.play()
            if music_volume==10:
                music_volume-=1
                choose_1_fx.play()
        if right_music_volume_but.draw(screen):
            if music_volume == 10:
                pass
            if music_volume == 9:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 8:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 7:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 6:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 5:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 4:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 3:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 2:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 1:
                music_volume += 1
                choose_2_fx.play()
            if music_volume == 0:
                music_volume += 1
                choose_2_fx.play()

        if left_music2_volume_but.draw(screen):
            if fx_volume==0:
                pass
            if fx_volume==1:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==2:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==3:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==4:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==5:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==6:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==7:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==8:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==9:
                fx_volume-=1
                choose_1_fx.play()
            if fx_volume==10:
                fx_volume-=1
                choose_1_fx.play()
        if right_music2_volume_but.draw(screen):
            if fx_volume == 10:
                pass
            if fx_volume == 9:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 8:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 7:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 6:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 5:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 4:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 3:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 2:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 1:
                fx_volume += 1
                choose_2_fx.play()
            if fx_volume == 0:
                fx_volume += 1
                choose_2_fx.play()

        draw_text(ver, font2, BLACK, 5, 770)


def select_level():
    global level_mode, main_menu_mode, start_game, level, player, health_bar, mana_bar, world,  music, score, start_intro, john_ammo, GRAVITY
    if level_mode==True:
        draw_bg()
        if back_but.draw(screen):
            level_mode=False
            main_menu_mode=True
        if lev1_but.draw(screen):
            level=1
            start_intro = True
            score=0
            john_ammo+=8
            if john_ammo>8:
                john_ammo=8
            time.sleep(0.4)
            GRAVITY=0.70
            level_mode=False
            start_game=True
            with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        world_data[x][y] = int(tile)
            world = World()
            player, health_bar, mana_bar = world.process_data(world_data)
            music = pygame.mixer.music.load('resource/common/sound/music/level1.mp3')
            music = pygame.mixer.music.play(-1, 0.0, 5000)
        if lev2_but.draw(screen):
            level=2
            time.sleep(0.4)
            john_ammo += 8
            if john_ammo > 8:
                john_ammo = 8
            score=0
            GRAVITY = 0.70
            start_intro = True
            level_mode=False
            start_game=True
            with open(f'levels/level{level}_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        world_data[x][y] = int(tile)
            world = World()
            player, health_bar, mana_bar = world.process_data(world_data)
            music = pygame.mixer.music.load('resource/common/sound/music/level2.mp3')
            music = pygame.mixer.music.play(-1, 0.0, 5000)

def shop():
    global shop_menu, main_menu_mode, alpha, fadein_start
    if shop_menu==True:
        screen.blit(shop_bg, (0,0))
        if lang==1:
            if closed_rus_button.draw(screen):
                shop_menu = False
                main_menu_mode = True
        if lang == 2:
            if closed_eng_button.draw(screen):
                shop_menu = False
                main_menu_mode = True
        if back_but.draw(screen):
            shop_menu=False
            main_menu_mode=True
            music = pygame.mixer.music.load('resource/common/sound/music/main.mp3')
            music = pygame.mixer.music.play(-1, 0.0, 5000)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

def reset_level():
    enemy_group.empty()
    boss_group.empty()
    schoolar_group.empty()
    bullet_group.empty()
    decoration_group.empty()
    chest_group.empty()
    decoration_group_front.empty()
    exit_group.empty()
    grass_group.empty()

    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)

    return data

def skin_changer():
    global skin_mode, main_menu_mode, john_skin_on
    if skin_mode==True:
        screen.blit(skin_changer_bg, (0,0))
        if john_skin_on==1:
            if john_1_skin_on_but.draw(screen):
                pass
            if john_2_skin_off_but.draw(screen):
                john_skin_on=2
            if john_3_skin_off_but.draw(screen):
                john_skin_on=3
        if john_skin_on==2:
            if john_1_skin_off_but.draw(screen):
                john_skin_on=1
            if john_2_skin_on_but.draw(screen):
                pass
            if john_3_skin_off_but.draw(screen):
                john_skin_on=3
        if john_skin_on==3:
            if john_1_skin_off_but.draw(screen):
                john_skin_on=1
            if john_2_skin_off_but.draw(screen):
                john_skin_on=2
            if john_3_skin_on_but.draw(screen):
                pass
        if john_soon_skin_but.draw(screen):
            pass
        if back_but.draw(screen):
            skin_mode=False
            main_menu_mode=True

class John(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        if john_skin_on==1:
            self.char_type='common'
        if john_skin_on==2:
            self.char_type='peppino'
        if john_skin_on==3:
            self.char_type='no_texture'
        self.speed=7
        self.ammo = 8
        self.start_ammo = 8
        self.shoot_cooldown = 0
        self.health = 200
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.x=x
        self.y=y
        self.reload_cooldown=30
        self.pig=False
        self.jump = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0


        animation_types = ['Idle', 'Run', 'Jump', 'Death', 'Idle_pig', 'Run_pig', 'Jump_pig']
        for animation in animation_types:

            temp_list = []

            num_of_frames = len(os.listdir(f'resource/common/img/john/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/john/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self, reload):
        self.update_animation()
        self.check_alive()

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if reload==True:
            if self.reload_cooldown>0:
                self.reload_cooldown-=1

    def move(self, moving_left, moving_right):

        screen_scroll = 0
        dx = 0
        dy = 0


        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            self.x-=1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
            self.x+=1

        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # if self.auto_jump == True and self.in_air == False:
        #     self.vel_y = -6.5
        #     self.auto_jump = False
        #     self.in_air = True


        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx=0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        if john_on==1:
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0

        self.rect.x += dx
        self.rect.y += dy

        if john_on==1:
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (
                    world.level_length * TILE_SIZE-10) - SCREEN_WIDTH) \
                    or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
                self.rect.x -= dx
                screen_scroll = -dx

        return screen_scroll, level_complete

    def reload(self, reload):
        global john_ammo, shoot
        if reload==True and self.reload_cooldown==0 and john_ammo<8:
            john_ammo+=1
            reload_shootgun_fx.play()
            self.reload_cooldown=35

    def shoot(self):
        global john_ammo
        if self.shoot_cooldown == 0 and john_ammo > 0 and self.pig==False:
            john_ammo-=1
            self.shoot_cooldown = 50
            self.reload_cooldown=35
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery + 25,self.direction)
            bullet_group.add(bullet)
            bullet = Bullet_up(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery + 25,self.direction)
            bullet_group.add(bullet)
            bullet = Bullet_down(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery + 25,self.direction)
            bullet_group.add(bullet)
            shoot_shootgun_fx.play()
            particles2.append([[self.rect.x, self.rect.y], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])
        if self.shoot_cooldown == 0 and john_ammo ==0 and self.pig == False:
            empty_fx.play()
            self.shoot_cooldown = 50
    def piggeria(self):
        global pig_time, music, boss_fight, level
        if self.pig==True:
            pig_time-=1
            if pig_time//5:
                if self.health<self.max_health:
                    self.health+=0.1
                if self.health==self.max_health:
                    self.health=self.max_health
            if pig_time<=0:
                self.pig=False
                if boss_fight==False:
                    a=level
                    print(a)
                    music = pygame.mixer.music.load(f'resource/common/sound/music/level{a}.mp3')
                    music = pygame.mixer.music.play(-1, 0.0, 5000)
                braah_voice2.play()

    def ai(self):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1:
                self.update_action(0)  # 0: idle
                self.idling = True
                self.idling_counter = 50
            if self.vision.colliderect(player.rect):
                self.update_action(0)  # 0: idle
                # shoot
                self.shoot()
            else:
                if self.idling == False:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        self.rect.x += screen_scroll

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Vlad(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='vlad'
        self.speed=5
        self.health=70
        self.max_health=self.health
        self.direction = 1
        self.scale = 1
        self.vel_y = 0
        self.jump = False
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 250, 5)
        self.attack_hitbox=300
        self.idling = False
        self.idling_counter = 0

        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'vlad':
                    if self.in_air == False:
                        self.jump = True
                    # self.direction *= -1
                    # self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.shoot()
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 30
            bullet = Plevok(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery + 25,
                            self.direction)
            bullet_group.add(bullet)
            plevok_fx.play()
            particles2.append([[self.rect.x, self.rect.y], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance = random.randint(1, 4)
            if chance == 1:
                erotic_voice.play()
            if chance == 2:
                wtf_voice.play()
            if chance == 3:
                postrelay_voice.play()
            if chance == 4:
                terrorist_win_voice.play()
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Pidor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='pidor'
        self.speed=5.5
        self.health=100
        self.max_health=self.health
        self.direction = 1
        self.scale = 3
        self.vel_y = 0
        self.jump = False
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 5)
        self.attack_hitbox=375
        self.idling = False
        self.idling_counter = 0

        animation_types = ['Idle', 'Run', 'Jump', 'Death', 'Shoot']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'pidor':
                    if self.in_air == False:
                        self.jump = True
                    # self.direction *= -1
                    # self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.shoot()
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def shoot(self):
        if self.shoot_cooldown == 0:
            self.update_action(4)
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery + 0,
                            self.direction)
            bullet_group.add(bullet)
            shoot_fx.play()
            particles2.append([[self.rect.x, self.rect.y], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 125
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance = random.randint(1, 3)
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_builder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='goblin_builder'
        self.speed=5
        self.health=50
        self.timer=100
        self.max_health=self.health
        self.direction = 1
        self.scale=3
        self.vel_y = 0
        self.jump = False
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown=0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 1, 1)
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        self.attack()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.timer>0:
            self.timer-=1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'goblin_builder':
                    if self.in_air==False:
                        self.jump=True
                    #self.direction *= -1
                    #self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True


        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def ai(self):
        global enemy_number
        if self.alive and player.alive:
            if self.vision.colliderect(player.rect) and self.in_air==False:
                self.idling==True
            else:
                if self.idling == False and self.timer<=0:
                    chance = random.randint(1, 1600)
                    if chance == 1 and enemy_number<=14:
                        built_fx.play()
                        enemy = Goblin_house(self.rect.centerx + 35, self.rect.y + 100)
                        enemy_group.add(enemy)
                        enemy_number+=1
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def attack(self):
        pass

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_with_a_spear(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='goblin_spear'
        self.speed=speed
        self.health=50
        self.max_health=self.health
        self.direction = 1
        self.scale=3
        self.vel_y = 0
        self.jump = False
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown=0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 10, 1)
        self.attack_hitbox=100
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'goblin_spear':
                    if self.in_air==False:
                        self.jump=True
                    #self.direction *= -1
                    #self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True


        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.attack()
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def attack(self):
        global player
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 20
            if player.pig == False:
                player.health-=5

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 50
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance=random.randint(1, 3)
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_house(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='goblin_house'
        self.health=100
        self.max_health=self.health
        self.direction = 1
        self.scale=3
        self.vel_y = 0
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * self.scale), int(img.get_height() * self.scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y-55)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()

    def ai(self):
        global enemy_number
        if self.alive and player.alive:
            chance=random.randint(1,500)
            if chance ==1 and enemy_number<=15:
                enemy = Goblin_with_a_spear(self.rect.centerx +25, self.rect.y + 300, 3)
                enemy_group.add(enemy)
                enemy_number+=1

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 75
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.alive = False
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_killer(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = 'goblin_killer'
        self.speed = 3.5
        self.shoot_cooldown = 0
        self.health = 50
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.x=x
        self.y=y
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 400, 20)
        self.attack_hitbox=300
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death', 'Shoot']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'goblin_killer':
                    if self.in_air == False:
                        self.jump = True
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def shoot(self):
        if self.shoot_cooldown == 0 and self.in_air==False:
            self.shoot_cooldown = 40
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            bullet_group.add(bullet)
            shoot_fx.play()

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.update_action(4)
                self.shoot()

            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right=True
                    else:
                        ai_moving_right=False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance = random.randint(1, 3)
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_king(pygame.sprite.Sprite):       #TODO класс короля гоблинов
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.char_type='goblin_king'
        self.speed=2.2
        self.health=1000
        self.max_health=self.health
        self.direction=1
        self.scale=3
        self.vel_y=0
        self.jump=False
        self.summon=False
        self.x=x
        self.y=y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 7, 10)
        self.attack_hitbox=180
        self.idling = False
        self.idling_counter = 0

        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def healthbar_boss(self):
        if self.alive==True:
            ratio = self.health / self.max_health
            pygame.draw.rect(screen, BLACK, (18, 660 - 2, 1247, 44))
            pygame.draw.rect(screen, BLACK, (20, 660-2, 1247, 44))
            pygame.draw.rect(screen, GREEN, (20, 660, 1245 * ratio, 40))

    def update(self):
        self.update_animation()
        self.check_alive()
        self.healthbar_boss()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        screen_scroll = 0
        dx = 0
        dy = 0

        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

            # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                if self.char_type == 'goblin_king':
                    if self.in_air == False:
                        self.jump = True
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

            # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

            # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll

    def ai(self):
        global enemy_number
        if self.alive and player.alive:
            if self.health>250:
                summon_chance=random.randint(1,400)
                if summon_chance == 1 and enemy_number<=13:
                    enemy = Goblin_with_a_spear(self.rect.centerx+35, self.rect.y - 10, 3)
                    enemy_group.add(enemy)
                    enemy = Goblin_with_a_spear(self.rect.centerx-35, self.rect.y - 10, 3)
                    enemy_group.add(enemy)
                    enemy_number+=2
            if self.health<=250:
                summon_chance = random.randint(1, 300)
                if summon_chance == 1 and enemy_number<=12:
                    enemy = Goblin_with_a_spear(self.rect.centerx + 35, self.rect.y - 10, 3)
                    enemy_group.add(enemy)
                    enemy = Goblin_with_a_spear(self.rect.centerx - 35, self.rect.y - 10, 3)
                    enemy_group.add(enemy)
                    enemy = Goblin_with_a_spear(self.rect.centerx - 55, self.rect.y - 10, 3)
                    enemy_group.add(enemy)
                    enemy_number+=3
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.attack()
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                        # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

            # scroll
        self.rect.x += screen_scroll

    def attack(self):
        global player
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 15
            if player.pig == False:
                player.health -= 35

    def update_animation(self):
        ANIMATION_COOLDOWN = 250
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global boss_fight, music, enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Goblin_boss(pygame.sprite.Sprite):
    def __init__(self,x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = 'goblin_boss'
        self.speed = 1
        self.health = 200
        self.max_health = self.health
        self.direction = 1
        self.scale = scale
        self.vel_y = 0
        self.jump = False
        self.x = x
        self.y = y
        self.in_air = True
        self.flip = False
        self.shoot_cooldown = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 9, 5)
        self.attack_hitbox=120
        self.idling = False
        self.idling_counter = 0

        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -10
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.char_type == 'goblin_boss':
                    if self.in_air == False:
                        self.jump = True
                    # self.direction *= -1
                    # self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                self.attack()
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def attack(self):
        global player
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 50
            if player.pig==False:
                player.health -= 75

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 250
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global boss_fight, music, enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance = random.randint(1, 3)
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Red_soldier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = 'red_soldier'
        self.speed = 3
        self.shoot_cooldown = 0
        self.health = 75
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.x=x
        self.y=y
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 350, 1)
        self.attack_hitbox=225
        self.idling = False
        self.idling_counter = 0

        # load all images for the players
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'resource/common/img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'resource/common/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * 3), int(img.get_height() * 3)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # jump
        if self.jump == True and self.in_air == False:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if the ai has hit a wall then make it turn around
                if self.in_air == False:
                    self.jump = True
                if self.char_type == 'enemy':
                    self.direction *= -1
                    self.move_counter = 0
            # check for collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if below the ground, i.e. jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground, i.e. falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True

        # check if fallen off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        return screen_scroll, level_complete

    def shoot(self):
        if self.shoot_cooldown == 0 and self.in_air==False:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            bullet_group.add(bullet)
            shoot_fx.play()

    def ai(self):
        if self.alive and player.alive:
            if self.rect.x-player.rect.x<=self.attack_hitbox and self.rect.x-player.rect.x>=-self.attack_hitbox and self.in_air==False:
                # stop running and face the player
                self.update_action(0)  # 0: idle
                # shoot
                self.shoot()
                a=random.randint(1,100)
                if a==1:
                    self.vision.colliderect(player.rect)
            else:
                if self.idling == False:
                    if self.rect.x < player.rect.x:
                        ai_moving_right=True
                    else:
                        ai_moving_right=False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1: run
                    self.move_counter += 1
                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out the reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        global enemy_number
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            chance = random.randint(1, 3)
            enemy_number-=1
            self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class World():
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data):
        global john_on
        self.level_length = len(data[0])
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile==0:
                        self.obstacle_list.append(tile_data)
                    elif  tile==1:
                        self.obstacle_list.append(tile_data)
                    elif tile==2:
                        self.obstacle_list.append(tile_data)
                    elif tile==3 or tile ==4:
                        self.obstacle_list.append(tile_data)
                    elif tile==5:
                        decoration=Decoration(img, x*TILE_SIZE, y*TILE_SIZE)
                        decoration_group_front.add(decoration)
                    elif tile==6:  #трава
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group_front.add(decoration)
                    elif tile==7:
                        pass
                    elif  tile==8:
                        self.obstacle_list.append(tile_data)
                    elif tile==9:
                        decoration=Decoration(img, x*TILE_SIZE, y*TILE_SIZE)
                        decoration_group_front.add(decoration)
                    elif tile == 10:
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group.add(decoration)
                    elif  tile==11:
                        self.obstacle_list.append(tile_data)
                    elif  tile==12:
                        self.obstacle_list.append(tile_data)
                    elif tile==13:
                        if level==1:
                            enemy=Goblin_with_a_spear(x * TILE_SIZE, y * TILE_SIZE, speed=3)
                            enemy_group.add(enemy)
                        if level==2:
                            enemy = Red_soldier(x * TILE_SIZE, y * TILE_SIZE)
                            enemy_group.add(enemy)
                    elif tile==14:
                        spawner=Spawner(img, x*TILE_SIZE, y*TILE_SIZE)
                        decoration_group.add(spawner)
                    if tile==15:
                        self.obstacle_list.append(tile_data)
                    elif  tile==16:
                        self.obstacle_list.append(tile_data)
                    elif tile == 17:
                        if john_on==1:
                            player = John( x * TILE_SIZE, y * TILE_SIZE, 3, 6)
                            health_bar = HealthBar(10, 10, player.health, player.max_health)
                            mana_bar = ManaBar(10, 35, mana)
                    elif  tile==18:
                        self.obstacle_list.append(tile_data)
                    elif tile==19:
                        self.obstacle_list.append(tile_data)
                    elif tile==20:
                        self.obstacle_list.append(tile_data)
                    elif tile==21:
                        self.obstacle_list.append(tile_data)
                    elif tile==22:
                        self.obstacle_list.append(tile_data)

        return player, health_bar, mana_bar

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll

class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        self.health = health
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 247, 24))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 247, 20))
        pygame.draw.rect(screen, RED, (self.x, self.y, 245, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 245 * ratio, 20))

class ManaBar():
    def __init__(self, x, y, mana):
        self.x = x
        self.y = y
        self.mana=mana

    def draw(self, mana):
        self.mana=mana
        ratio = self.mana / 100
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 247, 20))
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 247, 24))
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 245 * ratio, 20))

class Spawner(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        global level, boss_fight, score, enemy_number
        if level==2 and enemy_number <= 15:
            spawn=random.randint(1,100000)
            if spawn in range (2, 15+score) and boss_fight==False:
                enemy=Red_soldier(self.rect.centerx, self.rect.y+10)
                enemy_group.add(enemy)
            elif spawn in range(50000, 50015) and boss_fight==False:
                enemy = Pidor(self.rect.centerx, self.rect.y + 10)
                enemy_group.add(enemy)
            elif spawn in range(50016, 50030) and boss_fight==False:
                schoolar=Vlad(self.rect.centerx, self.rect.y + 10)
                schoolar_group.add(schoolar)
        if level == 1 and enemy_number <= 15:
            spawn = random.randint(1, 100000)
            if spawn in range(50000, 50010) and boss_fight == False:
                enemy = Goblin_boss(self.rect.centerx, self.rect.y + 10, 2.5, 1)
                enemy_group.add(enemy)
                enemy_number += 1
            if score <= 250:
                if spawn in range(2, 18 + score) and boss_fight == False:
                    chance = random.randint(1, 4)
                    if chance == 1 or chance == 2:
                        enemy = Goblin_with_a_spear(self.rect.centerx, self.rect.y + 10, 3)
                        enemy_group.add(enemy)
                        enemy_number += 1
                    if chance == 3:
                        enemy = Goblin_with_a_spear(self.rect.centerx, self.rect.y + 10, 3)
                        enemy_group.add(enemy)
                        enemy_number += 1
                    if chance == 4:
                        pass
            else:
                if spawn in range(2, 270) and boss_fight == False:
                    chance = random.randint(1, 3)
                    if chance == 1 or chance == 2:
                        enemy = Goblin_with_a_spear(self.rect.centerx, self.rect.y + 10, 3)
                        enemy_group.add(enemy)
                        enemy_number += 1
                    if chance == 3:
                        pass
            if spawn in range(7000, 7015) and boss_fight == False:
                enemy = Goblin_builder(self.rect.centerx, self.rect.y + 10)
                enemy_group.add(enemy)
                enemy_number += 1
            if spawn in range(8000, 8030) and boss_fight == False:
                enemy = Goblin_killer(self.rect.centerx, self.rect.y + 10)
                enemy_group.add(enemy)
                enemy_number += 1
            elif spawn in range(1, 4) and score >= 20:
                if boss_fight == False:
                    boss = Goblin_king(self.rect.centerx, self.rect.y + 10)
                    boss_group.add(boss)
                    music = pygame.mixer.music.load('resource/common/sound/music/boss1.wav')
                    music = pygame.mixer.music.play(-1, 0.0, 5000)
                    boss_fight = True
                    enemy_number += 1
        self.rect.x += screen_scroll

class Bullet_up(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        global score, mana, john_on, boss_fight
        self.rect.x += (self.direction * self.speed) + screen_scroll
        self.rect.y += (-2)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                for i in range(15):
                    particles3.append(
                        [[self.rect.x+screen_scroll, self.rect.y + 30+screen_scroll], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 15
                if player.health<=0:
                    braah_voice.play()
                for i in range(30):
                    particles.append(
                        [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()
        for boss in boss_group:
            if pygame.sprite.spritecollide(boss, bullet_group, False):
                if boss.alive:
                    boss.health-=25
                    if boss.health<=0:
                        score += random.randint(3,10)
                        mana += random.randint(10,25)
                        if mana >= 100:
                            mana = 100
                        if boss_fight == True:
                            music = pygame.mixer.music.load(f'resource/common/sound/music/level{level}.mp3')
                            music = pygame.mixer.music.play(-1, 0.0, 5000)
                            boss_fight=False
                    for i in prange(45):
                        particles.append(
                            [[self.rect.x+30, self.rect.y+30], [random.randint(0, 50) / 30 - 1, -1], random.randint(4, 6)])
                    self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    if enemy.health<=0:
                        a=random.randint(1,6)
                        score+=1
                        mana+=5
                        if mana>=100:
                            mana=100
                        if john_on==1:
                            if a==1:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                ti_she_voice.play()
                            if a==2:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                lox_voice.play()
                            if a==3:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                easy_voice.play()
                            else:
                                pass
                    for i in prange(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()
        for schoolar in schoolar_group:
            if pygame.sprite.spritecollide(schoolar, bullet_group, False):
                if schoolar.alive:
                    schoolar.health -= 25
                    if schoolar.health<=0:
                        score+=1
                        mana+=10
                        if mana>=100:
                            mana=100
                    for i in range(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()

class Bullet_down(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        global score, mana, john_on, boss_fight
        self.rect.x += (self.direction * self.speed) + screen_scroll
        self.rect.y += (2)
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                for i in range(15):
                    particles3.append(
                        [[self.rect.x, self.rect.y + 30+screen_scroll], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()


        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 15
                if player.health<=0:
                    braah_voice.play()
                for i in range(30):
                    particles.append(
                        [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()
        for boss in boss_group:
            if pygame.sprite.spritecollide(boss, bullet_group, False):
                if boss.alive:
                    boss.health-=25
                    if boss.health<=0:
                        score += random.randint(3,10)
                        mana += random.randint(10,25)
                        if mana >= 100:
                            mana = 100
                        if boss_fight == True:
                            music = pygame.mixer.music.load(f'resource/common/sound/music/level{level}.mp3')
                            music = pygame.mixer.music.play(-1, 0.0, 5000)
                            boss_fight=False
                    for i in range(45):
                        particles.append(
                            [[self.rect.x+30, self.rect.y+30], [random.randint(0, 50) / 30 - 1, -1], random.randint(4, 6)])
                    self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    if enemy.health<=0:
                        a=random.randint(1,6)
                        score+=1
                        mana+=5
                        if mana>=100:
                            mana=100
                        if john_on==1:
                            if a==1:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                ti_she_voice.play()
                            if a==2:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                lox_voice.play()
                            if a==3:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                easy_voice.play()
                            else:
                                pass
                    for i in range(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()
        for schoolar in schoolar_group:
            if pygame.sprite.spritecollide(schoolar, bullet_group, False):
                if schoolar.alive:
                    schoolar.health -= 25
                    if schoolar.health<=0:
                        score+=1
                        mana+=10
                        if mana>=100:
                            mana=100
                    for i in range(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        global score, mana, john_on, boss_fight
        self.rect.x += (self.direction * self.speed) + screen_scroll
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                for i in range(15):
                    particles3.append(
                        [[self.rect.x, self.rect.y + 30+screen_scroll], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 15
                if player.health<=0:
                    braah_voice.play()
                for i in range(30):
                    particles.append(
                        [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()
        for boss in boss_group:
            if pygame.sprite.spritecollide(boss, bullet_group, False):
                if boss.alive:
                    boss.health-=25
                    if boss.health<=0:
                        score += random.randint(5,20)
                        mana += random.randint(10,25)
                        if mana >= 100:
                            mana = 100
                        a=random.randint(1,3)
                        if john_on==1:
                            if a==1:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                ti_she_voice.play()
                            if a==2:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                lox_voice.play()
                            if a==3:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                easy_voice.play()
                        if boss_fight == True:
                            music = pygame.mixer.music.load(f'resource/common/sound/music/level{level}.mp3')
                            music = pygame.mixer.music.play(-1, 0.0, 5000)
                            boss_fight=False
                    for i in range(45):
                        particles.append(
                            [[self.rect.x+30, self.rect.y+30], [random.randint(0, 50) / 30 - 1, -1], random.randint(4, 6)])
                    self.kill()
        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    if enemy.health<=0:
                        a=random.randint(1,6)
                        score+=1
                        mana+=3
                        if mana>=100:
                            mana=100
                        if john_on==1:
                            if a==1:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                ti_she_voice.play()
                            if a==2:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                lox_voice.play()
                            if a==3:
                                ti_she_voice.stop()
                                lox_voice.stop()
                                easy_voice.stop()
                                easy_voice.play()
                            else:
                                pass
                    for i in range(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()
        for schoolar in schoolar_group:
            if pygame.sprite.spritecollide(schoolar, bullet_group, False):
                if schoolar.alive:
                    schoolar.health -= 25
                    if schoolar.health<=0:
                        score+=1
                        mana+=10
                        if mana>=100:
                            mana=100
                    for i in range(30):
                        particles.append(
                            [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                    self.kill()

class Plevok(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 7
        self.image = plevok_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        global score, mana, john_on, boss_fight
        self.rect.x += (self.direction * self.speed) + screen_scroll
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 15
                if player.health<=0:
                    braah_voice.play()
                for i in range(30):
                    particles.append(
                        [[self.rect.x, self.rect.y+30], [random.randint(0, 20) / 30 - 1, -1], random.randint(4, 5)])
                self.kill()


class ScreenFade():
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:
            pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour,
                             (SCREEN_WIDTH // 2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))
            pygame.draw.rect(screen, self.colour,
                             (0, SCREEN_HEIGHT // 2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
        if self.direction == 2:
            pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH*2, 0 + self.fade_counter))
        if self.fade_counter >= SCREEN_WIDTH:
            fade_complete = True

        return fade_complete

intro_fade = ScreenFade(1, BLACK, 4)
death_fade = ScreenFade(2, BLACK, 7)

go_r_but=button.Button(250, 500, go_r_img, 2)
go_l_but=button.Button(10, 500, go_l_img, 2)
jump_but=button.Button(1070, 500, jump_img, 2)
shoot_but=button.Button(850, 300, shoot_img, 2)
reload_but=button.Button(1100, 250, reload_img, 1.3)
ctrl_but=button.Button(15, 270, ctrl_img, 1)
shift_but=button.Button(15, 150, shift_img, 1)
back2_but=button.Button(15,15, back2_img, 3)

lev1_but=button.Button(50, 250, lev1_img, 10)
lev2_but=button.Button(350, 250, lev1_img, 10)
start_rus_button = button.Button(5, 350, start_rus_img, 1)
start_eng_button = button.Button(5, 350, start_eng_img, 1)
shop_rus_but=button.Button(5,430, shop_rus_img,  1)
shop_eng_but=button.Button(0,430, shop_eng_img,  1)
shop_bg1=button.Button(0,0, shop_bg, 1.8)
back_but=button.Button(15,15, back_img, 3)
exit_rus_but=button.Button(5,580, exitgame_rus, 1)
exit_eng_but=button.Button(5,580, exitgame_eng, 1)
settings_rus_but=button.Button(3,500, settings_rus_img, 1)
settings_eng_but=button.Button(3,510, settings_eng_img, 1)
score_but=button.Button(450,5, score_img, 11)
skin_but=button.Button(1150, 600, skin_img, 3)

john_1_skin_on_but=button.Button(50,200, john_1_skin_on, 3)
john_1_skin_off_but=button.Button(50,200, john_1_skin_off,3)

john_2_skin_on_but=button.Button(250,200, john_2_skin_on, 3)
john_2_skin_off_but=button.Button(250,200, john_2_skin_off,3)

john_3_skin_on_but=button.Button(450,200, john_3_skin_on, 3)
john_3_skin_off_but=button.Button(450,200, john_3_skin_off,3)

john_soon_skin_but=button.Button(650, 200, john_soon_skin, 3)

closed_rus_button=button.Button(300,100, closed_rus_img, 5)
closed_eng_button=button.Button(300,100, closed_eng_img, 5)

sound_rus_but=button.Button(550, 300, sound_rus, 1)
sound_eng_but=button.Button(530, 300, sound_eng, 1)

music_eng_but=button.Button(530, 100, music_eng, 1)

video_rus_but=button.Button(530, 400, video_rus, 1)
video_eng_but=button.Button(530, 400, video_eng, 1)

game_rus_but=button.Button(550, 200, game_rus, 1)
game_eng_but=button.Button(550, 200, game_eng, 1)

left_but=button.Button(550, 190, left_img, 2)
right_but=button.Button(750, 190, right_img, 2)

left_music_volume_but=button.Button(520, 180, left_img, 2)
right_music_volume_but=button.Button(710, 180, right_img, 2)

left_music2_volume_but=button.Button(520, 380, left_img, 2)
right_music2_volume_but=button.Button(710, 380, right_img, 2)

left_video_volume_but=button.Button(520, 300, left_img, 2)
right_video_volume_but=button.Button(770, 300, right_img, 2)

rus_but=button.Button(635, 196, rus_img, 2)
eng_but=button.Button(635, 196, eng_img, 2)

shootgun_ammo0=button.Button(0,75, shootgun_ammo0_img, 4)
shootgun_ammo1=button.Button(0,75, shootgun_ammo1_img, 4)
shootgun_ammo2=button.Button(0,75, shootgun_ammo2_img, 4)
shootgun_ammo3=button.Button(0,75, shootgun_ammo3_img, 4)
shootgun_ammo4=button.Button(0,75, shootgun_ammo4_img, 4)
shootgun_ammo5=button.Button(0,75, shootgun_ammo5_img, 4)
shootgun_ammo6=button.Button(0,75, shootgun_ammo6_img, 4)
shootgun_ammo7=button.Button(0,75, shootgun_ammo7_img, 4)
shootgun_ammo8=button.Button(0,75, shootgun_ammo8_img, 4)

enemy_group = pygame.sprite.Group()
boss_group=pygame.sprite.Group()
schoolar_group=pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
decoration_group_front = pygame.sprite.Group()
chest_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
grass_group = pygame.sprite.Group()

world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)

enemy_data = []
for row in range(ROWS):
    r = [-1] * COLS
    enemy_data.append(r)

run = True
while run:
    if fullscreen == 0 and screen_update == True:
        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN, pygame.SCALED)
        screen_update = False
    if fullscreen == 1 and screen_update == True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen_update = False
    clock.tick(FPS)

    if start_game == False:
        for i in range(0, tiles_bg1):
            screen.blit(bg_menu1, (i * bg_width1 + scroll_bg1, 0))
            bg_rect1.x = i * bg_width1 + scroll_bg1

        scroll_bg1 -= 2

        if abs(scroll_bg1) > bg_width1:
            scroll_bg1 = 0
        for i in range(0, tiles_bg2):
            screen.blit(bg_menu2, (i * bg_width2 + scroll_bg2, 100))
            bg_rect2.x = i * bg_width2 + scroll_bg2

        scroll_bg2 -= 1.6

        if abs(scroll_bg2) > bg_width2:
            scroll_bg2 = 0
        for i in range(0, tiles_bg3):
            screen.blit(bg_menu2, (i * bg_width3 + scroll_bg3, 300))
            bg_rect3.x = i * bg_width3 + scroll_bg3

        scroll_bg3 -= 1.4

        if abs(scroll_bg3) > bg_width3:
            scroll_bg3 = 0
        main_menu()
        select_level()
        shop()
        settings()
        settings_game()
        settings_video()
        settings_sound()
        skin_changer()
    else:
        player.piggeria()
        player.reload(reload=reload)

        #x_mouse, y_mouse=pygame.mouse.get_pos()
        if mobile_version==False:
            if pygame.mouse.get_pressed()[0] == 1:
                shoot=True
            if pygame.mouse.get_pressed()[0] == 0:
                shoot=False

        draw_bg()
        world.draw()

        chest_group.update()
        chest_group.draw(screen)
        decoration_group.update()
        decoration_group.draw(screen)

        for enemy in enemy_group:
            enemy.ai()
            enemy.update()
            enemy.draw()
        for schoolar in schoolar_group:
            schoolar.ai()
            schoolar.update()
            schoolar.draw()

        bullet_group.update()
        player.update(reload=reload)
        player.draw()
        decoration_group_front.update()
        exit_group.update()
        grass_group.update()
        bullet_group.draw(screen)
        for boss in boss_group:
            boss.ai()
            boss.update()
            boss.draw()
        decoration_group_front.draw(screen)

        if score_but.draw(screen):
            pass
        draw_text(f'{score}', font1, WHITE, 480, 5)
        if john_on==True:
            if john_ammo==8:
                if shootgun_ammo8.draw(screen):
                    pass
            if john_ammo==7:
                if shootgun_ammo7.draw(screen):
                    pass
            if john_ammo==6:
                if shootgun_ammo6.draw(screen):
                    pass
            if john_ammo==5:
                if shootgun_ammo5.draw(screen):
                    pass
            if john_ammo==4:
                if shootgun_ammo4.draw(screen):
                    pass
            if john_ammo==3:
                if shootgun_ammo3.draw(screen):
                    pass
            if john_ammo==2:
                if shootgun_ammo2.draw(screen):
                    pass
            if john_ammo==1:
                if shootgun_ammo1.draw(screen):
                    pass
            if john_ammo==0:
                if shootgun_ammo0.draw(screen):
                    pass

        health_bar.draw(player.health)
        mana_bar.draw(mana)

        if start_intro == True:
            if intro_fade.fade():
                start_intro = False
                intro_fade.fade_counter = 0
        if player.alive:

            if shoot:
                player.shoot()
            if player.pig==False:
                if player.in_air:
                    player.update_action(2)  # 2: jump
                elif moving_left or moving_right:
                    player.update_action(1)  # 1: run
                else:
                    player.update_action(0)  # 0: idle
            else:
                if player.in_air:
                    player.update_action(6)  # 2: jump
                elif moving_left or moving_right:
                    player.update_action(5)  # 1: run
                else:
                    player.update_action(4)  # 0: idle
            screen_scroll, level_complete = player.move(moving_left, moving_right)
            bg_scroll -= screen_scroll
            if level_complete:

                level += 1
                bg_scroll = 0
                world_data = reset_level()
                if level <= MAX_LEVELS:

                    with open(f'level{level}_data.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar, mana_bar, boss_bar  = world.process_data(world_data)
        else:
            screen_scroll = 0
            if death_fade.fade():
                death_fade.fade_counter = 0
                start_intro = True
                bg_scroll = 0
                world_data = reset_level()
                start_game=False
                main_menu_mode=True

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(screen, (255, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

    for particle in particles3:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        particle[1][1] += 0.2
        pygame.draw.circle(screen, BROWN, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles3.remove(particle)

    for particle in particles4:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(screen, YELLOW, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles4.remove(particle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_data.save()
            save_data.add('john_skin_on', john_skin_on)
            save_data.add('fullscreen', fullscreen)
            save_data.add('lang', lang)
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                reload=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                reload=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if fullscreen == 0:
                    fullscreen = 1
                    continue
                if fullscreen == 1:
                    fullscreen = 0
                    continue
            if event.key==pygame.K_F1:
                if lang==1:
                    lang=2
                    continue
                if lang==2:
                    lang=1
                    continue
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if start_game == True:
                if event.key==pygame.K_LSHIFT and player.alive:
                    if john_on==1:
                        if mana>=25:
                            mana-=25
                            player.health+=25
                            if player.health>player.max_health:
                                player.health=player.max_health
                            continue
                if event.key == pygame.K_LCTRL and player.alive:
                    if john_on==1:
                        if mana==100:
                            mana-=100
                            if mana<0:
                                mana=0
                            player.pig=True
                            pig_time=1800
                            braah_voice.play()
                            if boss_fight==False:
                                music=pygame.mixer.music.stop()
                                pig_theme.play()

            if event.key == pygame.K_SPACE and start_game==True:
                player.jump=True
            if event.key == pygame.K_ESCAPE:
                if skin_mode==True:
                    skin_mode=False
                    main_menu_mode=True
                    continue
                if settings_game_mode==True:
                    settings_game_mode=False
                    settings_mode=True
                    continue
                if settings_video_mode==True:
                    settings_video_mode=False
                    settings_mode=True
                    continue
                if settings_sound_mode==True:
                    settings_sound_mode=False
                    settings_mode=True
                    continue
                if main_menu_mode==True:
                    save_data.save()
                    save_data.add('john_skin_on', john_skin_on)
                    save_data.add('fullscreen', fullscreen)
                    save_data.add('lang', lang)
                    run=False
                if settings_mode==True:
                    settings_mode=False
                    main_menu_mode=True
                if level_mode==True:
                    level_mode=False
                    main_menu_mode=True
                if start_game==True:
                    start_game=False
                    main_menu_mode=True
                    world_data = reset_level()
                    screen_scroll=0
                    bg_scroll=0
                if shop_menu==True:
                    shop_menu=False
                    main_menu_mode=True
                    music = pygame.mixer.music.load('resource/common/sound/music/main.mp3')
                    music = pygame.mixer.music.play(-1, 0.0, 5000)

        if click==True:
            shoot=True
            player.reload=False
        else:
            shoot=False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE and start_game==True:
                player.jump=False
            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False

    if mobile_version==True and start_game==True:
        if go_r_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                moving_right = True
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                moving_right = False
        if go_l_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                moving_left = True
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                moving_left = False
        if jump_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                player.jump=True
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                player.jump = False
        if shoot_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                shoot=True
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                shoot = False
        if reload_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                reload=True
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                reload = False
        if shift_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                if john_on == 1:
                    if mana >= 25:
                        mana -= 25
                        player.health += 25
                        if player.health > player.max_health:
                            player.health = player.max_health
                        continue
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                pass
        if ctrl_but.draw(screen):
            if pygame.mouse.get_pressed()[0] == 1:
                if john_on == 1:
                    if mana == 100:
                        mana -= 100
                        if mana < 0:
                            mana = 0
                        player.pig = True
                        pig_time = 1800
                        braah_voice.play()
                        if boss_fight == False:
                            music = pygame.mixer.music.stop()
                            pig_theme.play()
        else:
            if pygame.mouse.get_pressed()[0] == 0:
                pass
        if back2_but.draw(screen):
            start_game=False
            main_menu_mode=True
            world_data = reset_level()
            screen_scroll = 0
            bg_scroll = 0

    pygame.display.update()


save_data.save()
save_data.add('john_skin_on', john_skin_on)
save_data.add('fullscreen', fullscreen)
save_data.add('lang', lang)
save_data.add('music_volume', music_volume)
save_data.add('fx_volume', fx_volume)
save_data.add('voice_volume', voice_volume)
pygame.quit()