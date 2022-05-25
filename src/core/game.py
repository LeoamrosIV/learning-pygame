#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Game class.
"""
import sys

import pygame as pg

from data import (SCREEN_RES, GAME_TITLE, MAX_FPS,
                  get_sprite, get_font)

from entities import Entity


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
        self.score_pos = (20, SCREEN_RES.height - 40)

        self.sky = Entity(get_sprite("background", "sky.png"))
        self.ground = Entity(get_sprite("background", "ground.png"), topleft=(0, self.sky.rect.height))

        self.player = Entity(get_sprite("player", "player_stand.png"),
                             midbottom=(50, self.ground.rect.y))

        self.snail = Entity(get_sprite("snail", "snail1.png"),
                            midbottom=(SCREEN_RES.width, self.ground.rect.y))

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
            self._check_collisions()

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

            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.snail.rect.collidepoint(event.pos):
                    self.score += 5

    def _update_screen(self) -> None:
        """
        Draws elements on screen.
        """
        self.sky.blit(self.screen)
        self.ground.blit(self.screen)

        score_surface = self.font.render(f"Score: {self.score}", False, "White")
        self.screen.blit(score_surface, self.score_pos)

        self.player.blit(self.screen)
        self.snail.blit(self.screen)

        if self.snail.rect.right <= 0:
            self.snail.rect.left = SCREEN_RES.width
        else:
            self.snail.rect.x -= 1

        # Draw elements on display
        pg.display.update()

    def _check_collisions(self) -> None:
        """
        Checks if objects are colliding.
        """
        if self.player.rect.colliderect(self.snail.rect):
            self.score += 5

    @staticmethod
    def _is_quit_button(event: pg.event.Event) -> bool:
        """
        Checks if an event to quit the game has been triggered.

        :param event: Captured event.
        :return: `True` if user triggered a quit event.
        """
        return event.type == pg.QUIT or (event.type == pg.KEYUP and event.dict["key"] == pg.K_ESCAPE)
