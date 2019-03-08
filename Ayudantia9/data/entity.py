import stddraw

from . import constants as c


class Drawable:

    def _draw(self):
        pass


class Entity(Drawable):

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y
        self.jumping = False
        self.falling = False
        self.size = .05

    def tick(self):
        pass

    def gravity(self):
        self.falling = True
        for block in self.map.blocks:
            if block.isOver(self) is True:
                if block.y1 < self.y and block.iscolliding(entity=self):
                    self.y += .001
                self.falling = False
                break
        if self.falling and not self.jumping:
            self.y -= c.MARIO_SPEED * 2

    def iscolliding(self, block=None, xcorrection=.0, ycorrection=.0, x1correction=.0, y1correction=.0):
        if block is not None:
            return True if block.iscolliding(self) is True else False
        for block in self.map.blocks:
            if block.iscolliding(self, float(xcorrection), ycorrection, x1correction, y1correction) is True:
                return True

    def kill(self):
        self.x = -9
        self.y = -9
        self.map.mario.score += 100


class FireFlower(Entity):
    def __init__(self, map, x, y):
        super().__init__(map, x, y)
        self.up = False
        self.moved = 1
        self.size = 0.005

    def _draw(self):
        stddraw.setPenColor(stddraw.ORANGE)
        stddraw.point(self.x, self.y)

    def tick(self):
        self.x += 0.003
        if self.up:
            self.y += 0.006
            self.moved += 1
            if self.moved == 10:
                self.up = False
        else:
            over = False
            for b in self.map.blocks:
                if b.isOver(self) and not over:
                    over = True
            if not over:
                self.y -= 0.01
            self.moved -= 1
            if self.moved == 0:
                self.up = True
            self.gravity()
        if self.iscolliding():
            self.kill()
        for enemy in self.map.enemies:
            if self.x > enemy.x and enemy.x - self.x < .01 and enemy.y - self.y < .01:
                enemy.kill()
        self._draw()
