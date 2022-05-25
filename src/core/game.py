#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Game class.
"""
import sys

import pygame as pg

from data import (SCREEN_RES, GAME_TITLE, MAX_FPS,
                  P, PTuple,
                  get_sprite, get_font)


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
        self.score = 0
        self.score_pos = PTuple(20, SCREEN_RES.height - 40)

        self.sky = get_sprite("background", "sky.png")
        self.sky_pos = PTuple(0, 0)
        self.ground = get_sprite("background", "ground.png")
        self.ground_pos = PTuple(0, self.sky.get_size()[1])

        self.player = get_sprite("player", "player_stand.png")
        self.player_rect = self.player.get_rect(midbottom=(50, self.ground_pos[1]))

        self.snail = get_sprite("snail", "snail1.png")
        self.snail_rect = self.snail.get_rect(midbottom=(SCREEN_RES.width, self.ground_pos[1]))

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
        self.screen.blit(self.sky, self.sky_pos)
        self.screen.blit(self.ground, self.ground_pos)
        self.screen.blit(self.player, self.player_rect)

        score_surface = self.font.render(f"Score: {self.score}", False, "White")
        self.screen.blit(score_surface, self.score_pos)

        self.screen.blit(self.snail, self.snail_rect)
        if self.snail_rect.right <= 0:
            self.snail_rect.left = SCREEN_RES.width
        else:
            self.snail_rect.x -= 1

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
