#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `PauseState` class, which is the game state
that freezes `PlayState`.
"""
import pygame as pg
from pygame.locals import *

from data import PAUSE_KEY, SCREEN_RES, SCREEN_CENTER, get_font

from .state import GameState


class PauseState(GameState):

    # Re-implemented abstract methods from base class

    def _init(self):
        self._text_alpha = 16
        self._background_alpha = 2

    def _loop(self, dt):
        pass

    def _process_event(self, event, dt):
        if event.type == KEYDOWN:
            if event.key == PAUSE_KEY:
                self._game.resume_game()

    def _update_screen(self):
        self.screen.blit(*self._get_background_surf())
        self.screen.blit(*self._get_pause_surf())
        self.screen.blit(*self._get_hint_surf())

    # Own methods

    def _get_background_surf(self) -> tuple[pg.Surface, pg.Rect]:
        """
        Returns a surface and a rect that represents pause screen background.

        :return: A tuple containing background surface and rect.
        """
        background = pg.Surface(SCREEN_RES)
        background.set_alpha(self._background_alpha)
        background.fill("white")
        return background, background.get_rect(topleft=(0, 0))

    def _get_pause_surf(self) -> tuple[pg.Surface, pg.Rect]:
        """
        Returns a surface and a rect that represent a "PAUSE" text.

        :return: A tuple containing game over text surface and rect.
        """
        font = get_font(120)
        surf = font.render("PAUSE", False, "black")
        surf.set_alpha(self._text_alpha)
        return surf, surf.get_rect(center=SCREEN_CENTER)

    def _get_hint_surf(self) -> tuple[pg.Surface, pg.Rect]:
        """
        Returns a surface and a rect that represent a hint for
        the user that explains how to resume game.

        :return: A tuple containing hint surface and rect.
        """
        def key_name(key):
            return pg.key.name(key).upper()

        text = f"PRESS '{key_name(PAUSE_KEY)}' TO RESUME"

        font = get_font(40)
        surf = font.render(text, False, "black")
        surf.set_alpha(self._text_alpha)
        x, y = SCREEN_CENTER

        return surf, surf.get_rect(center=(x, y + 50))
