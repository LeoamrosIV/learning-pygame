#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains data classes.
"""
from typing import NamedTuple


class ScreenRes(NamedTuple):
    """
    Screen resolution (width, height).
    """
    width: int
    height: int
