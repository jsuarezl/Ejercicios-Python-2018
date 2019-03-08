import os
import time

import stddraw
from picture import Picture

from . import constants as c
from . import entity
from .entity import FireFlower
from .map import Block
from .mushroom import Flower


class Mario(entity.Entity):
    def __init__(self, map, x, y):
        entity.Entity.__init__(self, map, x, y)
        self.map = map
        self.x = float(x)
        self.y = float(y)
        self._tick = 0
        self.score = 0
        # estados de mario
        self.moving = True
        self.jumping = False
        self.jumped = False
        self.jump_height = 0
        self.sprinting = False
        self.colliding = False
        self.dead = False
        self.big = False
        # propiedades
        self.size = c.BIG_MARIO_SIZE if self.big else c.SMALL_MARIO_SIZE
        self.ending = False
        self.fire_flower = False
        self.keys_pressed = {}
        self.last_shoot = 0

    def _draw(self):
        stddraw.picture(Picture(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'res' + os.path.sep + (
            'mario.png' if not self.big else 'big_mario.png' if not self.fire_flower else 'super_mario.jpg')), self.x,
                        self.y)

    def tick(self):
        if stddraw.mousePressed():
            c.BLOCKS.append(Block(stddraw.mouseX(), stddraw.mouseY()))
            for b in c.BLOCKS:
                print(str(b) + ',')
            for i in range(1, 3):
                print()
        self._tick += 1
        self.gravity()
        if stddraw.hasNextKeyTyped():
            k = stddraw.nextKeyTyped()
            if k == stddraw.K_RIGHT and not self.ending:
                if self.iscolliding(xcorrection=self.size) is True:
                    self.colliding = True
                if not self.colliding:
                    if self.x >= .25:
                        self.map.move(c.MARIO_SPEED * 3 if self.sprinting else c.MARIO_SPEED)
                    else:
                        self.x += c.MARIO_SPEED * 3 if self.sprinting else c.MARIO_SPEED
                else:
                    self.colliding = False
            if k == stddraw.K_LEFT and not self.ending:
                if not self.x - self.size <= -1:
                    if self.iscolliding(xcorrection=-self.size) is True:
                        self.colliding = True
                    if not self.colliding:
                        self.x -= c.MARIO_SPEED * 3 if self.sprinting else c.MARIO_SPEED
                    else:
                        self.colliding = False
            if k == stddraw.K_a and not self.ending:
                if not self.jumping and not self.keys_pressed[stddraw.K_a] and not self.falling:
                    self.jumped = True
                    self.jumping = True
                self.keys_pressed[stddraw.K_a] = True
            else:
                self.keys_pressed[stddraw.K_a] = False
            if k == stddraw.K_s and not self.keys_pressed[stddraw.K_s] and not self.ending:
                if not self.fire_flower:
                    self.sprinting = True
                elif self.last_shoot < int(round(time.time())):
                    self.map.fire_flowers.append(FireFlower(self.map, self.x, self.y))
                    self.last_shoot = time.time() + .2
                self.keys_pressed[stddraw.K_s] = True
            else:
                if not self.fire_flower:
                    self.sprinting = False
                self.keys_pressed[stddraw.K_s] = False
            if k == stddraw.K_q:
                self.dead = True
        for enemy in self.map.enemies:
            if enemy.x + .0125 >= self.x >= enemy.x - .0125:
                print(self.y, enemy.y + (.035 if self.big else .01))
                if self.y > enemy.y + (.035 if self.big else .01):  # correciones por la altura
                    if self.y - enemy.y + .01 < .05:
                        enemy.kill()
                        self.y += .05
                else:
                    if self.big:
                        self.big = False if self.big else True
                        self.size = c.BIG_MARIO_SIZE if self.big else c.SMALL_MARIO_SIZE
                        self.fire_flower = False
                    else:
                        self.dead = True
        for mushroom in self.map.mushrooms:
            if mushroom.x - self.x < .02 and mushroom.y - self.y < .02:
                if not isinstance(mushroom, Flower):
                    self.big = False if self.big else True
                    self.size = c.BIG_MARIO_SIZE if self.big else c.SMALL_MARIO_SIZE
                    self.y += c.BIG_MARIO_SIZE
                else:
                    self.fire_flower = True
                    self.sprinting = True
                mushroom.kill()
        if self.jumping:  # manejo de salto
            bcollision = False
            for block in self.map.blocks:
                if not block.collided and block.iscolliding(self, y1correction=self.size) and not bcollision:
                    block.collide(self)
                    bcollision = True
            if self.jumped and self.jump_height < c.JUMP_HEIGHT:
                if not self.iscolliding(y1correction=self.size):
                    self.y += (c.MARIO_SPEED * 2) if not self.sprinting else (c.MARIO_SPEED * 3)
                self.jump_height += 1
            if self.jump_height >= c.JUMP_HEIGHT:
                self.jumped = False
            if self.jump_height > 0 and not self.jumped:
                if not self.falling and not self.iscolliding(ycorrection=self.size + .01):
                    self.y -= c.MARIO_SPEED * 2
                self.jump_height -= 1
            if self.jump_height == 0 and not self.jumped:
                self.jumping = False
            self._draw()
        if self.y <= -1:
            self.dead = True
        self._draw()

    def iscolliding(self, block=None, xcorrection=.0, ycorrection=.0, x1correction=.0, y1correction=.0):
        entity.Entity.iscolliding(self, block)
        if block is not None:
            return True if block.iscolliding(self) is True else False
        for block in self.map.blocks:
            if block.iscolliding(self, float(xcorrection), ycorrection, x1correction, y1correction) is True:
                return True
