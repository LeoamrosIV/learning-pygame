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
        self.__active = State.MENU                       # type: State

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

    def new_game(self) -> None:
        """
        Starts a new game.
        """
        assert self.__active in (State.MENU, State.GAME_OVER)
        self.__states[State.PLAYING] = PlayState(self._game)
        self.set_state(State.PLAYING)

    def resume_game(self) -> None:
        """
        Resumes the current game.
        """
        assert self.__active in (State.PAUSE, State.MENU)
        self.set_state(State.PLAYING)

    def main_menu(self) -> None:
        """
        Goes to main menu.
        """
        assert self.__active is not State.MENU
        self.set_state(State.MENU)

    def pause_game(self) -> None:
        """
        Pauses the game.
        """
        assert self.__active is State.PLAYING
        self.set_state(State.PAUSE)

    def game_over(self) -> None:
        """
        Ends the current game.
        """
        assert self.__active is State.PLAYING
        self.set_state(State.GAME_OVER)
