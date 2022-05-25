#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains base entity classes.
"""
import pygame as pg


class Entity:
    """
    Base class for every game entity.
    """

    def __init__(self, surface: pg.Surface, **pos: tuple[int, int]):
        if not pos:
            pos = {"topleft": (0, 0)}

        assert len(pos) == 1
        self.__surf = surface                      # type: pg.Surface
        self.__rect = self.__surf.get_rect(**pos)  # type: pg.Rect

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
