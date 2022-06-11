#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains paths to assets directories.
"""
import os

# Directories
CONST_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.realpath(os.path.join(CONST_DIR, "..", ".."))
ASSETS_DIR = os.path.join(SRC_DIR, "assets")
GRAPHICS_DIR = os.path.join(ASSETS_DIR, "graphics")
AUDIO_DIR = os.path.join(ASSETS_DIR, "audio")
FONT_DIR = os.path.join(ASSETS_DIR, "font")
