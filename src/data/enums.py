#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains game `Enums`.
"""
from enum import Enum


class State(Enum):
    """
    An enumerator for different game states.
    """
    MENU = 0
    PLAYING = 1
    PAUSE = 2
    GAME_OVER = 3
