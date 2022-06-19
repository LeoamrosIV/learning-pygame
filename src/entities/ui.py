#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains entity classes useful for ui composition.
"""
import pygame as pg

from .base import Entity


class Button(Entity):
    """A button that can be pressed to call a function."""

    def __init__(self, surface: pg.Surface, color: tuple[int, int, int], callback: callable, active: bool = False, focused: bool = False):
        super().__init__(surface)
        self.active = active
        self.focused = focused
        self.color = color
        self.callback = callback

    @property
    def box(self) -> pg.Rect:
        """
        Returns the `Rect` representing the whole `Button` (with box).

        :return: Whole `Button`'s `Rect`.
        """
        box_rect = self.rect.inflate(20, 15)
        box_rect.y -= 4
        return box_rect

    def blit(self, surface: pg.Surface) -> None:
        """
        Draws `Entity` on given `surface`, using `self.surf`
        as a representation and `self.rect` as position.

        :param surface: A surface to draw `Entity` onto.
        """
        if self.active:
            bg_color = self.color
        else:
            attenuation = 32
            max_value = 255 - attenuation
            bg_color = tuple(n + attenuation if n <= max_value else 255 for n in self.color)

        box = self.box
        pg.draw.rect(surface, bg_color, box, border_radius=3)
        surface.blit(self.surf, self.rect)

        if self.focused:
            halo = box.inflate(5, 5)
            halo_color = "gold" if self.active else "silver"
            pg.draw.rect(surface, halo_color, halo, width=5, border_radius=3)

    def press(self):
        """
        Calls the callback if the button is active.
        """
        if self.active:
            self.callback()
