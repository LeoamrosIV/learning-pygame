#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains abstract class for game states.
"""
import sys

from abc import ABC, abstractmethod
from typing import Protocol

import pygame as pg

from data import State


class WrongState(Exception):
    """
    Raised when trying to set a non-existing state as active.
    """


class GameProtocol(Protocol):
    keys_pressed: dict[int, bool]
    screen: pg.Surface
    score: int
    def new_game(self) -> None: ...
    def resume_game(self) -> None: ...
    def main_menu(self) -> None: ...
    def pause_game(self) -> None: ...
    def game_over(self) -> None: ...


class GameState(ABC):
    """
    Abstract class for a game state.
    """

    def __init__(self, game: GameProtocol) -> None:
        self._game = game  # type: GameProtocol
        self._init()

    @property
    def keys_pressed(self) -> dict[int, bool]:
        return self._game.keys_pressed

    @property
    def screen(self) -> pg.Surface:
        return self._game.screen

    @property
    def score(self) -> int:
        return self._game.score

    @score.setter
    def score(self, v: int) -> None:
        self._game.score = v

    @abstractmethod
    def _init(self):
        """
        Initialize state.
        """

    def loop(self, dt: int) -> None:
        """
        Runs game loop.

        :param dt: delta time
        """
        self.process_events(dt)
        self._loop(dt)
        self.update_screen()

    @abstractmethod
    def _loop(self, dt: int) -> None:
        """
        Runs game loop.

        :param dt: delta time
        """

    def process_events(self, dt: int) -> None:
        """
        Processes game events.

        To be called at each iteration of the game loop.

        :param dt: delta time.
        """
        for event in pg.event.get():

            if event.type == pg.QUIT:
                # Exit the game
                sys.exit()

            self._process_event(event, dt)

    @abstractmethod
    def _process_event(self, event: pg.event.Event, dt: int) -> None:
        """
        Processes a game event

        :param event: event to process.
        :param dt: delta time.
        """

    def update_screen(self) -> None:
        """
        Draws elements on screen.
        """
        self._update_screen()

        # Draw elements on display
        pg.display.update()

    @abstractmethod
    def _update_screen(self) -> None:
        """
        Draws elements on screen.
        """
