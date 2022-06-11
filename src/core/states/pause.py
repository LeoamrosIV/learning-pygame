#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `PauseState` class, which is the game state
that freezes `PlayState`.
"""
import pygame as pg

from .state import GameState


class PauseState(GameState):

    # Re-implemented abstract methods from base class

    def _init(self):
        pass

    def _loop(self, dt):
        pass

    def _process_event(self, event: pg.event.Event, dt: int) -> None:
        pass

    def _update_screen(self) -> None:
        pass

    # Own methods
