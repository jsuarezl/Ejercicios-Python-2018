import os

import stddraw
from picture import Picture

from . import constants as c
from .entity import Entity


class Mushroom(Entity):
    def __init__(self, map, x, y):
        super().__init__(map, x, y)
        self.target = 0
        self.size = .01

    def _draw(self):
        stddraw.picture(
            Picture(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'res' + os.path.sep + 'mushroom.png'),
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
        super(Mushroom, self).kill()
        self.map.mario.score += 900


class Flower(Mushroom):
    def __init__(self, map, x, y):
        super().__init__(map, x, y)

    def _draw(self):
        stddraw.picture(
            Picture(os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'res' + os.path.sep + 'flower.png'),
            self.x, self.y)

    def tick(self):
        self.gravity()
        self._draw()
