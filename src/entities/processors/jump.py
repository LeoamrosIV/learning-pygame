#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains jump processors.
"""
from typing import Protocol, Type, Optional


class _Actor(Protocol):
    """Represents the needed entity interface for it to perform a jump."""
    gravity: float


class _JumpComponent(Protocol):
    """Represents the jump component interface"""
    name: str
    max_jumps: int
    jump_height: float
    multi_jump_tempo: float


class JumpProcessor:
    """
    Given an entity and a jump component,
    it can make the entity perform the jump
    represented by the jump component.
    """

    def __init__(self, entity: _Actor, *jump_components: Type[_JumpComponent]) -> None:
        self.__entity = entity                # type: _Actor
        self.__jumps = list(jump_components)  # type: list[Type[_JumpComponent]]
        self.__jumping = 0                    # type: int
        self.__active = None                  # type: Optional[Type[_JumpComponent]]
        if self.__jumps:
            self.__active = self.__jumps[0]

    def active(self) -> str:
        """
        Returns active jump name.
        """
        return self.__active.name

    def change_jump_type(self) -> None:
        """
        Sets the next jump component in `self.__jumps` as active.
        """
        if not self.__jumps:
            return

        assert self.__active is not None and self.__active in self.__jumps

        next_jump_idx = self.__jumps.index(self.__active) + 1
        if next_jump_idx >= len(self.__jumps):
            next_jump_idx = 0

        self.__active = self.__jumps[next_jump_idx]

    def jump(self) -> None:
        """
        The entity that owns the `Jump` instance,
        performs a jump if it can.
        """
        if self._can_jump():
            self._perform_jump()
            self.__jumping += 1

    def landed(self) -> None:
        """
        Resets self.__jumping to 0.
        """
        self.__jumping = 0
        self.__entity.gravity = 0

    def _can_jump(self) -> bool:
        """
        `True` if the entity that owns the `Jump` instance can jump atm.
        """
        if self.__active is None or self.__jumping >= self.__active.max_jumps:
            return False

        gravity_limit = 0 if not self.__jumping else self.__active.multi_jump_tempo
        return self.__entity.gravity >= gravity_limit

    def _perform_jump(self) -> None:
        """
        The entity that owns the `Jump` instance, performs a jump.
        """
        assert self.__active is not None
        self.__entity.gravity = - self.__active.jump_height
