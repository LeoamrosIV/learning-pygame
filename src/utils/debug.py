#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains debug functions.
"""
import pygame as pg
from typing import Callable, Any


def debug_func(f: Callable, default: Any = None):
    """
    Decorator for debug functions.

    Functions decorated with this are only called in debug mode.
    If not in debug mode, wrapped function always return `default` argument.

    :param f: Function to be wrapped.
    :param default: Default return value when not in debug mode.
    :return: Function that is executed only in debug mode.
    """
    def wrapper(*a, **kw):
        return f(*a, **kw) if __debug__ else default
    return wrapper


@debug_func
def print_event(e: pg.event.Event) -> None:
    print(f"({pg.event.event_name(e.type)} | {e.type}) >>> {e.dict}")
