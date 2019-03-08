import time

import stddraw
from color import Color

from . import constants as c
from .mushroom import Flower
from .mushroom import Mushroom


class Map:

    def __init__(self, blocks, enemies):
        self.x = 0
        self.blocks = list(blocks)
        self.moving = False
        self.enemies = list(enemies)
        self.mario = None
        self.mushrooms = []
        self.fire_flowers = []

    def draw(self):
        for block in self.blocks:
            block.draw()
        if self.mario is not None:
            stddraw.text(-.9, .9, 'Score: {}'.format(self.mario.score))

    def move(self, x):
        for enemy in self.enemies:
            enemy.x -= x
        for block in self.blocks:
            block.x -= x
        for mushroom in self.mushrooms:
            mushroom.x -= x
        for flower in self.fire_flowers:
            flower.x -= x

    def update(self):
        for enemy in self.enemies:
            if enemy.x < -1 or enemy.y < -1:
                self.enemies.remove(enemy)
                continue
            if enemy.x > 1:
                continue
            enemy.tick()
        for block in self.blocks:
            if block.x + block.x1 < -1 or block.y + block.y1 < -1:
                self.blocks.remove(block)
        for mushroom in self.mushrooms:
            if mushroom.x < -1 or mushroom.y < -1:
                self.mushrooms.remove(mushroom)
                continue
            mushroom.tick()
        for flower in self.fire_flowers:
            if flower.x < -1 or flower.y < -1:
                self.fire_flowers.remove(flower)
                continue
            flower.tick()
        self.draw()


class Block:

    def __init__(self, x, y, x1=.05, y1=.05, breakable=False, coins=0, color=stddraw.DARK_RED, mushroom=False):
        self.x = float(x)
        self.y = float(y)
        self.x1 = x1
        self.y1 = y1
        self.breakable = breakable
        self.coins = 0 if not breakable else coins
        self.color = color
        self.last_collision = 0
        self.collided = False
        self.mushroom = mushroom
        self.mushroom_spawned = False
        self.map = None

    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledRectangle(self.x, self.y, self.x1, self.y1)

    def isOver(self, entity):
        if entity.x > (self.x + self.x1) or entity.x < self.x:
            return None
        # if isinstance(entity, Enemy):
        #    print(entity.y - entity.size, self.y + self.y1,
        #          ((entity.y - entity.size) ** 2) ** (1 / 2) - ((self.y + self.y1) ** 2) ** (1 / 2), entity)
        return entity.y - entity.size > self.y + self.y1 and -.01 < ((entity.y - entity.size) ** 2) ** (1 / 2) - (
                (self.y + self.y1) ** 2) ** (1 / 2) < .01

    def iscolliding(self, entity, xcorrection=0, ycorrection=0, x1correction=0, y1correction=0):
        float(xcorrection)
        float(ycorrection)
        float(x1correction)
        float(y1correction)
        if entity.y - ycorrection > self.y + self.y1 or entity.y + y1correction < self.y:
            return None
        return self.x < entity.x + xcorrection < self.x + self.x1  # c.COLLISION <= self.x - x < 0 or

    def collide(self, mario):
        if self.last_collision == 0:
            self.last_collision = time.time() + .1
            if self.breakable:
                if self.coins == 0 and mario.size == c.BIG_MARIO_SIZE:
                    self._delete()
                if self.coins > 0:
                    self.coins -= 1
                    mario.score += 200
                    if self.coins == 0:
                        self.coins = -1
                        self.color = Color(186, 137, 0)
                        self.collided = True
                if self.mushroom:
                    self.mushroom = False
                    self.mushroom_spawned = True
                    if self.map.mario.big:
                        self.map.mushrooms.append(Flower(self.map, self.x, self.y + .07))
                    else:
                        self.map.mushrooms.append(Mushroom(self.map, self.x, self.y + .07))
        elif self.last_collision <= int(round(time.time())):
            self.last_collision = 0

    def _delete(self):
        self.x = -10
        self.y = -10
        self.x1 = -10
        self.y1 = -10

    def __str__(self):
        return "Block({}, {}, color={})".format(self.x, self.y, self.color)
