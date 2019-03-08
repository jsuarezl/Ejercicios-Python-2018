import stddraw

from ball import Ball


class Ladrillo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        if self.y == 0:
            stddraw.setPenColor(stddraw.RED)
        elif self.y == .1:
            stddraw.setPenColor(stddraw.BOOK_RED)
        elif self.y == .2:
            stddraw.setPenColor(stddraw.DARK_RED)
        elif self.y == .3:
            stddraw.setPenColor(stddraw.ORANGE)
        elif self.y == .4:
            stddraw.setPenColor(stddraw.YELLOW)
        elif self.y == .5:
            stddraw.setPenColor(stddraw.GREEN)
        elif self.y == .6:
            stddraw.setPenColor(stddraw.DARK_GREEN)
        elif self.y == .7:
            stddraw.setPenColor(stddraw.BLUE)
        elif self.y == .8:
            stddraw.setPenColor(stddraw.DARK_BLUE)
        elif self.y == .9:
            stddraw.setPenColor(stddraw.BOOK_BLUE)
        stddraw.filledRectangle(self.x, self.y, .1, .1)


class Barra:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.filledRectangle(self.x, self.y, .15, .05)


ladrillos = []

for y in range(0, 10):
    for x in range(-10, 10):
        nx = float(x) / 10
        ny = float(y) / 10
        ladrillos.append(Ladrillo(nx, ny))

stddraw.setCanvasSize(500, 500)

stddraw.setXscale(-1, 1)
stddraw.setYscale(-1, 1)

b = Ball(.075, -.9, .015, .015, .025, stddraw.RED)
barra = Barra(0, -1)

stddraw.setFontSize(16)

while not b.moving:
    if stddraw.hasNextKeyTyped():
        k = stddraw.nextKeyTyped()
        if k == stddraw.K_SPACE:
            b.moving = True
    stddraw.clear(stddraw.WHITE)
    stddraw.text(0, 0, 'Press space to start')
    stddraw.show(0)
    stddraw.pause(20)

while not b.bot:
    # get keystrokes
    if stddraw.hasNextKeyTyped():
        k = stddraw.nextKeyTyped()
        if k == stddraw.K_LEFT:
            barra.x -= .05
        elif k == stddraw.K_RIGHT:
            b.increase_speed(-0.1, -0)
            barra.x += .05

    b.update(ladrillos, barra)
    # clear the background
    stddraw.clear(stddraw.LIGHT_GRAY)

    # draw the ball on the screen
    b.draw()
    barra.draw()

    for ladrillo in ladrillos:
        ladrillo.draw()

    # copy buffer to screen
    stddraw.show(0)
    stddraw.pause(20)
while b.bot:
    stddraw.clear(stddraw.WHITE)
    stddraw.text(0, 0, 'WELL PLAYED')
    stddraw.show(0)
    stddraw.pause(20)
    if stddraw.hasNextKeyTyped():
        exit(0)
