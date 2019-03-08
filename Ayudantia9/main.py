import os

import stddraw

from data import constants as c
from data.enemy import Enemy
from data.enemy import Turtle
from data.map import Map
from data.mario import Mario


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    if not stddraw._windowCreated:
        stddraw.setCanvasSize(800, 600)
        stddraw.setXscale(-1.0, 1.0)
        stddraw.setYscale(-1.0, 1.0)
    m = Map(c.BLOCKS, [])
    for b in m.blocks:
        b.map = m
    mario = Mario(m, c.SPAWN_POINT[0], c.SPAWN_POINT[1])
    m.draw()
    m.mario = mario

    def createenemies():
        return [Enemy(m, 0, -.7), Enemy(m, .5, -.7), Enemy(m, .7, -.7), Enemy(m, .65, -.7),
                Turtle(m, 2, -.7),
                Enemy(m, 2.05, -.7), Enemy(m, 2.1, -.7)]

    m.enemies = createenemies()
    while not mario.dead:
        stddraw.clear(stddraw.LIGHT_GRAY)
        m.update()
        mario.tick()
        stddraw.show(0)
        stddraw.pause(20)


if __name__ == '__main__':
    main()
