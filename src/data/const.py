#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains constants.
"""
import os

from . import Area

SCREEN_RES = Area(800, 400)
GAME_TITLE = "Sup?"
MAX_FPS = 60

ASSETS_DIR = "assets"
GRAPHICS_DIR = os.path.join(ASSETS_DIR, "graphics")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
FONT_DIR = os.path.join(ASSETS_DIR, "font")
