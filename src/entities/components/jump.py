#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains jump components.
"""
from abc import ABC
from dataclasses import dataclass


@dataclass
class JumpComponent(ABC):
    """
    Generic jump component.
    """
    name: str
    max_jumps: int
    jump_height: float
    multi_jump_tempo: float


@dataclass
class BaseJump(JumpComponent):
    """
    The most basic type of jump.
    """
    name = "Jump"
    max_jumps = 1
    jump_height = 25.
    multi_jump_tempo = 0


@dataclass
class DoubleJump(JumpComponent):
    """
    A jump where you can jump a second time in midair.
    """
    name = "Double Jump"
    max_jumps = 2
    jump_height = 22.
    multi_jump_tempo = 7.


@dataclass
class JetpackJump(JumpComponent):
    """
    A jump that simulates a jetpack.
    """
    name = "Jetpack"
    max_jumps = 25
    jump_height = 10.
    multi_jump_tempo = -8.
