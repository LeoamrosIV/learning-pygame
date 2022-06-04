#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains base entity classes.
"""
from typing import Protocol, Iterable, Optional
from abc import ABC

import pygame as pg

from data import GRAVITY
from .processors import JumpProcessor


class _JumpComponent(Protocol):
    """Represents the jump component interface"""
    name: str
    max_jumps: int
    jump_height: float
    multi_jump_tempo: float


class Entity(ABC):
    """
    Base class for every game entity.
    """

    def __init__(self, surface: pg.Surface):
        self.__surf = surface                 # type: pg.Surface
        self.__rect = self.__surf.get_rect()  # type: pg.Rect

    @property
    def surf(self) -> pg.Surface:
        """
        Returns entity surface.
        """
        return self.__surf

    @property
    def rect(self) -> pg.Rect:
        """
        Returns entity rect.
        """
        return self.__rect

    def blit(self, surface: pg.Surface) -> None:
        """
        Draws `Entity` on given `surface`, using `self.surf`
        as a representation and `self.rect` as position.

        :param surface: A surface to draw `Entity` onto.
        """
        surface.blit(self.surf, self.rect)


class StaticEntity(Entity):
    """A static entity that doesn't move."""


class Actor(Entity):
    """An animate entity."""

    def __init__(self, surface: pg.Surface, jump_components: Optional[Iterable[_JumpComponent]] = None) -> None:
        super().__init__(surface)
        self.gravity = 0.                                              # type: float

        if jump_components is None:
            jump_components = ()

        self.__jump_processor = JumpProcessor(self, *jump_components)  # type: JumpProcessor

    def move(self, x: float = 0., y: float = 0.) -> None:
        """
        Updates entity position.

        :param x: x movement.
        :param y: y movement.
        """
        self.rect.move_ip(x, y)

    def jump(self) -> None:
        self.__jump_processor.jump()

    def landed(self) -> None:
        self.__jump_processor.landed()

    def apply_gravity(self, dt: int) -> None:
        self.gravity += GRAVITY * dt
        self.move(y=self.gravity)

    def change_jump_type(self) -> None:
        """
        Changes active jump type for this entity.
        """
        self.__jump_processor.change_jump_type()

    def get_jump_type(self) -> str:
        """
        Returns active jump name.
        """
        return self.__jump_processor.active()
