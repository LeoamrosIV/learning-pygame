#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `Game` class.
"""
import pygame as pg

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
        self.score = 0                           # type: int

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

    def _reset_keys_pressed(self):
        """
        Sets all pressed keys to `False`.
        """
        for key in self.keys_pressed:
            self.keys_pressed[key] = False

    def new_game(self) -> None:
        """
        Starts a new game.
        """
        self._reset_keys_pressed()
        self.state_manager.new_game()

    def resume_game(self) -> None:
        """
        Resumes the current game.
        """
        self._reset_keys_pressed()
        self.state_manager.resume_game()

    def main_menu(self) -> None:
        """
        Goes to main menu.
        """
        self._reset_keys_pressed()
        self.state_manager.main_menu()

    def pause_game(self) -> None:
        """
        Pauses the game.
        """
        self._reset_keys_pressed()
        self.state_manager.pause_game()

    def game_over(self) -> None:
        """
        Ends the current game.
        """
        self._reset_keys_pressed()
        self.state_manager.game_over()
