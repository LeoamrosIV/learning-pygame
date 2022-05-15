#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains functions to import sprites.
"""
import os

import pygame as pg

from . import GRAPHICS_DIR, FONT_DIR


_alpha_for_sprite_group = {
    "background": False,
    "player": True,
    "fly": True,
    "snail": True,
}


def get_sprite(group: str, name: str) -> pg.Surface:
    """
    Given the name of the sprites group and the name of the sprite,
    returns a pg.Surface with that image.

    :param group: Folder name.
    :param name: Sprite name.
    :return: Selected sprite.
    """
    assert group in _alpha_for_sprite_group, f"Only this groups accepted: {list(_alpha_for_sprite_group)}"
    alpha = _alpha_for_sprite_group[group]
    raw_img = pg.image.load(os.path.join(GRAPHICS_DIR, group, name))
    return raw_img.convert_alpha() if alpha else raw_img.convert()


def get_font(size: int, default: bool = False) -> pg.font.Font:
    """
    Returns game font at the selected size.

    :param size: Font size.
    :param default: If True, use default pygame font.
    :return: Game font.
    """
    font_name = None if default else os.path.join(FONT_DIR, "Pixeltype.ttf")
    return pg.font.Font(font_name, size)
