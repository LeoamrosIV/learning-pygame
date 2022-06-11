#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains settings and constants about display, gameplay etc.
"""
from .. import Area as _Area

# Display
SCREEN_RES = _Area(800, 400)
SCREEN_CENTER = (SCREEN_RES.width // 2, SCREEN_RES.height // 2)
GAME_TITLE = "Sup?"
MAX_FPS = 60

# Gameplay
GRAVITY = 0.11
