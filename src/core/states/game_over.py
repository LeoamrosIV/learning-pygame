#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `GameOverState` class, which is the game state
that shows game over screen.
"""
import pygame as pg
from pygame.locals import *

from data import SCREEN_RES, SCREEN_CENTER, get_font
from data.const.keybindings import RESTART_KEY, MENU_KEY

from entities import StaticEntity

from .state import GameState


class GameOverState(GameState):

    # Re-implemented abstract methods from base class

    def _init(self):
        self._text_alpha = 16
        self._background_alpha = 8

    def _loop(self, dt):
        pass

    def _process_event(self, event, dt):
        if event.type == KEYDOWN:
            if event.key == RESTART_KEY:
                self._game.new_game()

            elif event.key == MENU_KEY:
                self._game.main_menu()

    def _update_screen(self):
        for ent in (self._get_background_surf(),
                    self._get_game_over_surf(),
                    self._get_score_surf(),
                    self._get_hint_surf(),
                    ):
            ent.blit(self.screen)

    # Own methods

    def _get_background_surf(self) -> StaticEntity:
        """
        Returns a surface and a rect that represents game over screen background.

        :return: A tuple containing background surface and rect.
        """
        background = pg.Surface(SCREEN_RES)
        background.set_alpha(self._background_alpha)
        background.fill("black")
        return StaticEntity(background)

    def _get_game_over_surf(self) -> StaticEntity:
        """
        Returns a surface and a rect that represent a "GAME OVER" text.

        :return: A tuple containing game over text surface and rect.
        """
        font = get_font(120)
        surf = font.render("GAME OVER", False, "white")
        surf.set_alpha(self._text_alpha)
        x, y = SCREEN_CENTER

        game_over = StaticEntity(surf)
        game_over.rect.center = (x, y - 60)
        return game_over

    def _get_score_surf(self) -> StaticEntity:
        """
        Returns a surface and a rect that show the final score to the user.

        :return: A tuple containing score surface and rect.
        """
        text = f"FINAL SCORE: {self.score}"
        font = get_font(60)
        surf = font.render(text, False, "white")
        surf.set_alpha(self._text_alpha)

        score = StaticEntity(surf)
        score.rect.center = SCREEN_CENTER
        return score

    def _get_hint_surf(self) -> StaticEntity:
        """
        Returns a surface and a rect that represent a hint for
        the user that explains how to start a new game.

        :return: A tuple containing hint surface and rect.
        """
        def key_name(key):
            return pg.key.name(key).upper()

        text = f"PRESS '{key_name(RESTART_KEY)}' TO RESTART, " \
               f"'{key_name(MENU_KEY)}' TO GO TO MAIN MENU"

        font = get_font(40)
        surf = font.render(text, False, "white")
        surf.set_alpha(self._text_alpha)
        x, y = SCREEN_CENTER

        hint = StaticEntity(surf)
        hint.rect.center = (x, y + 50)
        return hint
