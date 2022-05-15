#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains data classes.
"""
from typing import NamedTuple
from dataclasses import dataclass


class Area(NamedTuple):
    """
    Simple named tuple to represent an area (width, height).
    """
    width: int
    height: int


class PTuple(NamedTuple):
    """
    Simple named tuple to represent a point (x, y).
    """
    x: int
    y: int


@dataclass(order=True)
class P:
    """
    Simple dataclass to represent a point (x, y).
    """
    x: int
    y: int

    def __call__(self):
        return PTuple(self.x, self.y)
