#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains constants.
"""
import os

from . import Area

# Display
SCREEN_RES = Area(800, 400)
GAME_TITLE = "Sup?"
MAX_FPS = 60

# Directories
DATA_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.realpath(os.path.join(DATA_DIR, ".."))
ASSETS_DIR = os.path.join(SRC_DIR, "assets")
GRAPHICS_DIR = os.path.join(ASSETS_DIR, "graphics")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
FONT_DIR = os.path.join(ASSETS_DIR, "font")

# Gameplay
GRAVITY = 0.11
