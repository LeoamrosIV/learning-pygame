#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains functions to import sprites.
"""
import os

import pygame as pg

from . import GRAPHICS_DIR, FONT_DIR


def _get_sprite(*path: str, alpha: bool = False) -> pg.Surface:
    """
    Given a path to an image, returns a pg.Surface with that image.

    :param path: Path to sprite file.
    :param alpha: If True, allows transparency.
    :return: Selected sprite.
    """
    raw_img = pg.image.load(os.path.join(*path))
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


def get_background_sprite(name: str, alpha: bool = False) -> pg.Surface:
    """
    Returns the selected background sprite.

    :param name: Image name.
    :param alpha: If True, allows transparency.
    :return: Selected sprite.
    """
    return _get_sprite(GRAPHICS_DIR, "background", name, alpha=alpha)


