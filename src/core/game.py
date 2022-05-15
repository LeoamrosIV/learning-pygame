#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Game class.
"""
import sys

import pygame as pg

from data import (SCREEN_RES, GAME_TITLE, MAX_FPS,
                  Area, P, PTuple,
                  get_background_sprite, get_font)


class Game:
    """
    Main game class, starts and runs the game.
    """

    def __init__(self) -> None:
        # Initialize all imported pygame modules.
        pg.init()

        self._init_window()
        self._init_entities()
        self._run_game_loop()

    def _init_window(self) -> None:
        """
        Initialize window setting screen resolution and window title.
        """
        self.screen = pg.display.set_mode(SCREEN_RES)
        pg.display.set_caption(GAME_TITLE)

    def _init_entities(self) -> None:
        """
        Initializes persistent entities.
        """
        self.font = get_font(50)
        self.sky = get_background_sprite("sky.png")
        self.ground = get_background_sprite("ground.png")

    def _run_game_loop(self) -> None:
        """
        Runs the game loop.
        """
        clock = pg.time.Clock()

        while True:
            # Limit FPS and calculate delta time
            dt = clock.tick(MAX_FPS)
            self._process_events(dt)
            self._update_screen()

    def _process_events(self, dt: int) -> None:
        """
        Processes game events.

        To be called at each iteration of the game loop.

        :param dt: delta time.
        """
        for event in pg.event.get():

            if self._is_quit_button(event):
                # Exit the game
                sys.exit()

    def _update_screen(self) -> None:
        self.screen.blit(self.sky, PTuple(0, 0))
        self.screen.blit(self.ground, PTuple(0, self.sky.get_size()[1]))

        while True:
            # Limit FPS and calculate delta time
            dt = clock.tick(MAX_FPS)

            self._process_events(dt)

        # Draw elements on display
        pg.display.update()

    @staticmethod
    def _is_quit_button(event: pg.event.Event) -> bool:
        """
        Checks if an event to quit the game has been triggered.

        :param event: Captured event.
        :return: `True` if user triggered a quit event.
        """
        return event.type == pg.QUIT or (event.type == pg.KEYUP and event.dict["key"] == pg.K_ESCAPE)
