#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains data classes.
"""
from typing import NamedTuple


class Area(NamedTuple):
    """
    Simple named tuple to represent an area (width, height).
    """
    width: int
    height: int
