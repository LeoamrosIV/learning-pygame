#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `Game` class.
"""
import pygame as pg

from data import State
from data.const.settings import *
from data.const.keybindings import *

from .states import StateManager


class Game:
    """
    Main game class, starts and runs the game.
    """

    def __init__(self) -> None:
        # Initialize all imported pygame modules.
        pg.init()

        self.keys_pressed = {
            JUMP_KEY: False,
            MOVE_RIGHT_KEY: False,
            MOVE_LEFT_KEY: False,
        }                                        # type: dict[int, bool]

        self._init_window()

        self.state_manager = StateManager(self)  # type: StateManager
        self._run_game_loop()

    def _init_window(self) -> None:
        """
        Initialize window setting screen resolution and window title.
        """
        self.screen = pg.display.set_mode(SCREEN_RES)
        pg.display.set_caption(GAME_TITLE)

    def _run_game_loop(self) -> None:
        """
        Runs the game loop.
        """
        clock = pg.time.Clock()

        while True:
            # Limit FPS and calculate delta time
            dt = clock.tick(MAX_FPS)
            self.state_manager.active_state().loop(dt)

    def set_state(self, state: State) -> None:
        """
        Sets the active state of the game.

        :param state: the `State` to set as active.
        """
        self.state_manager.set_state(state)
