__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c


class Coin(pg.sprite.Sprite):
    """Flashing coin next to coin total info"""
    def __init__(self, get_fps, x, y):
        super(Coin, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.create_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.first_half = True
        self.frame_index = 0
        self.get_fps = get_fps


    def create_frames(self):
        """Extract coin images from sprite sheet and assign them to a list"""
        self.frames = []
        self.frame_index = 0

        self.frames.append(self.get_image(1, 160, 5, 8))
        self.frames.append(self.get_image(9, 160, 5, 8))
        self.frames.append(self.get_image(17, 160, 5, 8))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet"""
        image = pg.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self, current_frame):
        """Animates flashing coin"""
        if self.first_half:
            if self.frame_index == 0:
                if (current_frame - self.timer) > 375*self.get_fps/1000:
                    self.frame_index += 1
                    self.timer = current_frame
            elif self.frame_index < 2:
                if (current_frame - self.timer) > 125*self.get_fps/1000:
                    self.frame_index += 1
                    self.timer = current_frame
            elif self.frame_index == 2:
                if (current_frame - self.timer) > 125*self.get_fps/1000:
                    self.frame_index -= 1
                    self.first_half = False
                    self.timer = current_frame
        else:
            if self.frame_index == 1:
                if (current_frame - self.timer) > 125*self.get_fps/1000:
                    self.frame_index -= 1
                    self.first_half = True
                    self.timer = current_frame

        self.image = self.frames[self.frame_index]
