#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `MenuState` class, which is the game state
that shows the main menu.
"""
import sys

import pygame as pg

from data import get_font, get_sprite, SCREEN_RES, SCREEN_CENTER
from entities import StaticEntity, Button

from .state import GameState


class MenuState(GameState):

    # Re-implemented abstract methods from base class

    def _init(self):
        font = get_font(70)
        btn_color = (24, 59, 92)
        self.buttons = [
            Button(font.render("Continue", False, "white"), btn_color, self._game.resume_game, active=False),
            Button(font.render("New game", False, "white"), btn_color, self._game.new_game, active=True),
            Button(font.render("Exit game", False, "white"), btn_color, sys.exit, active=True),
        ]

        x_segment, y_segment = SCREEN_RES.width // 3, SCREEN_RES.height // 4

        x_btn, y_btn = x_segment * 2, y_segment
        for btn in self.buttons:
            btn.rect.center = (x_btn, y_btn)
            y_btn += y_segment

        logo = get_sprite("player", "player_stand.png")
        logo_res = tuple(n * 3 for n in logo.get_rect().size)
        logo = pg.transform.scale(logo, logo_res)

        self.logo = StaticEntity(logo)
        self.logo.rect.center = x_segment, SCREEN_CENTER[1]

    def _loop(self, dt):
        continue_btn = self.buttons[0]
        continue_btn.active = self._game.has_active_game()

    def _process_event(self, event, dt):
        if event.type == pg.MOUSEMOTION:
            for btn in self.buttons:
                if btn.box.collidepoint(event.pos):
                    self._set_focused(btn)
                    break
                else:
                    self._unfocus()

        elif event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
            for btn in self.buttons:
                if btn.focused:
                    btn.press()
                    break

    def _update_screen(self):
        self.screen.fill((94, 129, 162))
        self.logo.blit(self.screen)

        for btn in self.buttons:
            btn.blit(self.screen)

    # Own methods

    def _set_focused(self, button: Button) -> None:
        """
        Sets the currently focused button.

        :param button: The button to focus on.
        """
        assert button in self.buttons
        self._unfocus()
        button.focused = True

    def _unfocus(self) -> None:
        """
        Removes the focus from all the buttons.
        """
        for btn in self.buttons:
            btn.focused = False
