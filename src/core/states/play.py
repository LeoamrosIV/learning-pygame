#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contains `PlayState` class, which is the game state
in which the player can play the game.
"""
import pygame as pg
from pygame.locals import *

from data import get_sprite, get_font
from data.const.settings import *
from data.const.keybindings import *

from entities import StaticEntity, Actor
from entities.components import BaseJump, DoubleJump, JetpackJump, RocketJump

from .state import GameState


class PlayState(GameState):

    # Re-implemented abstract methods from base class

    def _init(self):
        self._init_entities()
        self._init_hud_elements()

    def _loop(self, dt):
        self._handle_movement(dt)
        self._check_collisions()

    def _process_event(self, event, dt):
        if event.type == KEYDOWN:
            self._handle_key_down(event.key)

        elif event.type == KEYUP:
            self._handle_key_up(event.key)

        elif event.type == WINDOWFOCUSLOST:
            self._game.pause_game()

        elif event.type == pg.MOUSEBUTTONDOWN:
            if self.snail.rect.collidepoint(event.pos):
                self.score += 5

    def _update_screen(self):
        self.sky.blit(self.screen)
        self.ground.blit(self.screen)

        self._update_hud()

        self.player.blit(self.screen)
        self.snail.blit(self.screen)

        mouse_pos = pg.mouse.get_pos()
        if self.snail.rect.collidepoint(mouse_pos):
            pg.draw.circle(self.screen, "gold", mouse_pos, 30, 5)

        if self.snail.rect.right <= 0:
            self.score += 100
            self.snail.rect.left = SCREEN_RES.width
        else:
            self.snail.rect.x -= 1

    # Own methods

    def _init_entities(self) -> None:
        """
        Initializes persistent entities.
        """
        self.sky = StaticEntity(get_sprite("background", "sky.png"))
        self.sky.rect.topleft = (0, 0)

        self.ground = StaticEntity(get_sprite("background", "ground.png"))
        self.ground.rect.topleft = (0, self.sky.rect.height)

        self.player = Actor(get_sprite("player", "player_stand.png"),
                            (BaseJump, DoubleJump, JetpackJump, RocketJump))
        self.player.rect.midbottom = (50, self.ground.rect.y)

        self.snail = Actor(get_sprite("snail", "snail1.png"))
        self.snail.rect.midbottom = (SCREEN_RES.width, self.ground.rect.y)

    def _init_hud_elements(self) -> None:
        """
        Initializes texts to draw on screen.
        """
        self.font = get_font(50)
        self.score = 0

        self.score_pos = (20, SCREEN_RES.height - 28)
        self.jump_info_pos = (SCREEN_RES.width // 2, 30)

        self.score_text = "Score: {}"
        self.jump_info_text = "Press [{}] to change jump type. Using: {}"

    def _update_hud(self) -> None:
        """
        Draws hud elements on screen.
        """
        score_surf = self.font.render(self.score_text.format(self.score), False, "black")
        score_rect = score_surf.get_rect(midleft=self.score_pos)
        score_bg_rect = score_rect.inflate(10, 10)
        score_bg_rect.y -= 4
        pg.draw.rect(self.screen, "bisque2", score_bg_rect, border_radius=3)
        self.screen.blit(score_surf, score_rect)

        jump_info_surf = self.font.render(self.jump_info_text.format(pg.key.name(CHANGE_JUMP_KEY).upper(),
                                                                     self.player.get_jump_type()),
                                          False, "black")

        jump_info_rect = jump_info_surf.get_rect(midtop=self.jump_info_pos)
        jump_info_bg_rect = jump_info_rect.inflate(10, 10)
        jump_info_bg_rect.y -= 4
        pg.draw.rect(self.screen, "azure", jump_info_bg_rect, border_radius=3)
        self.screen.blit(jump_info_surf, jump_info_rect)

    def _handle_movement(self, dt: int) -> None:
        """
        Handles player movement.

        :param dt: delta time.
        """
        x = 0

        # ----- Movement using pygame.key.get_pressed() ----- #
        # keys = pg.key.get_pressed()
        # x += int(keys[MOVE_RIGHT_KEY]) - int(keys[MOVE_LEFT_KEY])

        x += (int(self.keys_pressed[MOVE_RIGHT_KEY]) - int(self.keys_pressed[MOVE_LEFT_KEY])) * dt * 0.5
        if self.keys_pressed[JUMP_KEY]:
            self.player.jump()

        self.player.move(x=x)

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
            self._game.game_over()

        top_ground = self.ground.rect.top
        for ent in (self.player, self.snail):
            if top_ground < ent.rect.bottom:
                ent.rect.bottom = top_ground
                ent.landed()

    def _handle_key_down(self, key: int) -> None:
        """
        Handles `KEYDOWN` events.

        :param key: Pressed key.
        """
        if key in self.keys_pressed:
            self.keys_pressed[key] = True

        elif key is PAUSE_KEY:
            self._game.pause_game()

        elif key is MENU_KEY:
            self._game.main_menu()

    def _handle_key_up(self, key: int) -> None:
        """
        Handles `KEYUP` events.

        :param key: Released key.
        """
        if key in self.keys_pressed:
            self.keys_pressed[key] = False

        elif key == CHANGE_JUMP_KEY:
            self.player.change_jump_type()
