#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains Game class.
"""
import sys

import pygame as pg
from pygame.locals import *

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
        self._keys_pressed = {
            K_UP: False,
            K_RIGHT: False,
            K_LEFT: False,
        }
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
        self.score_pos = (20, SCREEN_RES.height - 28)

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
            self._handle_movement(dt)
            self._check_collisions()
            self._update_screen()

    def _process_events(self, dt: int) -> None:
        """
        Processes game events.

        To be called at each iteration of the game loop.

        :param dt: delta time.
        """
        for event in pg.event.get():

            if event.type == KEYDOWN:
                self._handle_key_down(event.key)

            elif event.type == KEYUP:
                self._handle_key_up(event.key)

            elif event.type == pg.MOUSEBUTTONDOWN:
                if self.snail.rect.collidepoint(event.pos):
                    self.score += 5

            elif event.type == pg.QUIT:
                # Exit the game
                sys.exit()

    def _update_screen(self) -> None:
        """
        Draws elements on screen.
        """
        self.sky.blit(self.screen)
        self.ground.blit(self.screen)

        score_surf = self.font.render(f"Score: {self.score}", False, "black")
        score_rect = score_surf.get_rect(midleft=self.score_pos)
        score_bg_rect = score_rect.inflate(10, 10)
        score_bg_rect.y -= 4
        pg.draw.rect(self.screen, "bisque2", score_bg_rect, border_radius=3)
        self.screen.blit(score_surf, score_rect)

        self.player.blit(self.screen)
        self.snail.blit(self.screen)

        mouse_pos = pg.mouse.get_pos()
        if self.snail.rect.collidepoint(mouse_pos):
            pg.draw.circle(self.screen, "gold", mouse_pos, 30, 5)

        if self.snail.rect.right <= 0:
            self.snail.rect.left = SCREEN_RES.width
        else:
            self.snail.rect.x -= 1

        # Draw elements on display
        pg.display.update()

    def _handle_movement(self, dt: int) -> None:
        """
        Handles player movement.

        :param dt: delta time.
        """
        x = y = 0

        # ----- Movement using pygame.key.get_pressed() ----- #
        # keys = pg.key.get_pressed()
        # x += int(keys[K_RIGHT]) - int(keys[K_LEFT])

        x += (int(self._keys_pressed[K_RIGHT]) - int(self._keys_pressed[K_LEFT])) * dt * 0.5
        y -= int(self._keys_pressed[K_UP]) * dt

        self.player.move(x=x, y=y)

        player_rect = self.player.rect
        if player_rect.left < 0:
            player_rect.left = 0
        elif player_rect.right > SCREEN_RES.width:
            player_rect.right = SCREEN_RES.width

        for ent in (self.player, self.snail):
            ent.apply_gravity(dt)

    def _check_collisions(self) -> None:
        """
        Checks if objects are colliding.
        """
        if self.player.rect.colliderect(self.snail.rect):
            self.score += 5

        top_ground = self.ground.rect.top
        for ent in (self.player, self.snail):
            if top_ground < ent.rect.bottom:
                ent.rect.bottom = top_ground
                ent.reset_gravity()

    def _handle_key_down(self, key: int) -> None:
        """
        Handles `KEYDOWN` events.

        :param key: Pressed key.
        """
        self._keys_pressed[key] = True

    def _handle_key_up(self, key: int) -> None:
        """
        Handles `KEYUP` events.

        :param key: Released key.
        """
        self._keys_pressed[key] = False
