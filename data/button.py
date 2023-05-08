import pygame
from pygame import mixer

mixer.init()

lev0_info = False
lev1_info = False


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Controller_button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Level_button():
    def __init__(self, x, y, image, act_img, mode, scale):
        width = image.get_width()
        self.mode = mode
        self.lev0_info = False
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.act_image = pygame.transform.scale(act_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        global lev0_info, lev1_info
        action = False
        act = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            act = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if act == False:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        if act == True:
            if self.mode == 0:
                lev0_info = True
            surface.blit(self.act_image, (self.rect.x, self.rect.y))

        return action


class Anim_button():
    def __init__(self, x, y, image, act_img, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.act_image = pygame.transform.scale(act_img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        act = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            act = True
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        if act == False:
            surface.blit(self.image, (self.rect.x, self.rect.y))
        if act == True:
            surface.blit(self.act_image, (self.rect.x, self.rect.y))

        return action