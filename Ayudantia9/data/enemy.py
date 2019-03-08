import os

import stddraw
from picture import Picture

from . import constants as c
from . import entity


class Enemy(entity.Entity):
    def __init__(self, map, x, y):
        entity.Entity.__init__(self, map, x, y)
        self.map = map
        self.x = x
        self.y = y
        self.size = .010
        self.target = 1

    def _draw(self):
        stddraw.picture(
            Picture(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'res' + os.path.sep + 'goomba.png'),
            self.x, self.y)

    def tick(self):
        if self.target == 1 and not self.iscolliding(xcorrection=-0.03):
            self.x -= c.ENEMY_SPEED
        else:
            self.target = 0
        if self.target == 0 and not self.iscolliding(x1correction=-0.03):
            self.x += c.ENEMY_SPEED
        else:
            self.target = 1
        self.gravity()
        self._draw()

    def kill(self):
        self.x = -9
        self.y = -9
        self.map.mario.score += 100


class Turtle(Enemy):
    def __init__(self, map, x, y):
        super().__init__(map, x, y)

    def _draw(self):
        stddraw.picture(
            Picture(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'res' + os.path.sep + 'turtle.png'),
            self.x, self.y)
