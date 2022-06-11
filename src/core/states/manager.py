#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `StateManager`.
"""
from . import (State, WrongState, GameState, GameProtocol,
               PlayState, GameOverState, MenuState, PauseState)


class StateManager:
    """
    An object used to manage the active state of the game.
    """

    def __init__(self, game: GameProtocol):
        self._game = game                                # type: GameProtocol
        self.__states = {
            State.MENU: MenuState(self._game),
            State.PLAYING: PlayState(self._game),
            State.PAUSE: PauseState(self._game),
            State.GAME_OVER: GameOverState(self._game),
        }                                                # type: dict[State: GameState]
        self.__active = State.PLAYING                    # type: State

    def set_state(self, state: State) -> None:
        """
        Sets the active state of the game.

        :param state: the `State` to set as active.
        """
        if state not in self.__states:
            raise WrongState()

        self.__active = state

    def active_state(self) -> GameState:
        """
        Returns the currently active `GameState`.

        :return: The active `GameState`.
        """
        return self.__states[self.__active]

