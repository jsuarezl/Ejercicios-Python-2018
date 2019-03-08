import stddraw

from .map import Block

MARIO_SPEED = .003
JUMP_HEIGHT = 20
SMALL_MARIO_SIZE = 0.015
BIG_MARIO_SIZE = 0.025
SPAWN_POINT = (-.80, -.6)
COLLISION = .001
ENEMY_SPEED = .0015
BLOCKS = [Block(-.50, -.70, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(-.30, -.70, breakable=True, color=stddraw.ORANGE),
          Block(-.25, -.70, breakable=True, coins=1, color=stddraw.YELLOW, mushroom=True),
          Block(-.20, -.70, breakable=True, color=stddraw.ORANGE),
          Block(-.15, -.70, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(-.10, -.70, breakable=True, color=stddraw.ORANGE),
          Block(-.20, -.55, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(-1, -1, 2, .20),
          Block(.05, -0.8, y1=.06, color=stddraw.DARK_GREEN),
          Block(0.28, -0.8, y1=.08, color=stddraw.DARK_GREEN),
          Block(0.55, -0.8, y1=.1, color=stddraw.DARK_GREEN),
          Block(0.8, -0.8, y1=.1, color=stddraw.DARK_GREEN),
          Block(1.1, -1, .5, .20),
          Block(1.2, -.70, breakable=True, color=stddraw.ORANGE),
          Block(1.25, -.70, breakable=True, coins=1, color=stddraw.YELLOW, mushroom=True),
          Block(1.3, -.70, breakable=True, color=stddraw.ORANGE),
          Block(1.35, -.55, x1=.3, breakable=False, color=stddraw.ORANGE),
          Block(1.7, -1, 2.3, .20),
          Block(1.75, -0.55, x1=.2, breakable=False, color=stddraw.ORANGE),
          Block(1.95, -.55, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(1.95, -.70, breakable=True, coins=5, color=stddraw.ORANGE),
          Block(2.05, -.70, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(2.25, -.70, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(2.35, -.55, breakable=True, coins=1, color=stddraw.YELLOW, mushroom=True),
          Block(2.35, -.70, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(2.45, -.70, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(2.60, -.70, breakable=True, color=stddraw.ORANGE),
          Block(2.75, -.55, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(3, -.55, breakable=True, color=stddraw.ORANGE),
          Block(3.05, -.55, breakable=True, coins=1, color=stddraw.YELLOW),
          Block(3.05, -.70, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(3.1, -.55, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(3.2, -.8, x1=.2, breakable=True, color=stddraw.ORANGE),
          Block(3.25, -.75, x1=.15, breakable=True, color=stddraw.ORANGE),
          Block(3.30, -.70, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(3.35, -.65, breakable=True, color=stddraw.ORANGE),
          Block(3.45, -.65, breakable=True, color=stddraw.ORANGE),
          Block(3.45, -.70, x1=.1, breakable=True, color=stddraw.ORANGE),
          Block(3.45, -.75, x1=.15, breakable=True, color=stddraw.ORANGE),
          Block(3.45, -.80, x1=.2, breakable=True, color=stddraw.ORANGE),
          Block(3.75, -.80, x1=.25, breakable=True, color=stddraw.ORANGE),
          Block(3.80, -.75, x1=.2, breakable=True, color=stddraw.ORANGE),
          Block(3.85, -.70, x1=.15, breakable=True, color=stddraw.ORANGE),
          Block(3.90, -.65, x1=.1, breakable=True, color=stddraw.ORANGE)]
