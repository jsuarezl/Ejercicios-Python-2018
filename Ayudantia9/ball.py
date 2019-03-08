import stddraw


class Ball:
    def __init__(self, rx, ry, vx, vy, radius, color):
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.moving = False
        self.bot = False

    def update(self, ladrillos, barra):
        """
        Bounce of wall according to elastic collition and
        update velocity.
        """
        if not self.moving:
            return
        for l in ladrillos:
            if l.x <= self.rx <= l.x + .1 and l.y <= self.ry <= l.y + .1:
                self.vx = -self.vx
                self.vy = -self.vy
                ladrillos.remove(l)
                continue
        if abs(self.rx + self.vx) + self.radius > 1.0:
            self.vx = -self.vx
        if self.ry + self.vy - self.radius < -1:
            if barra.x <= self.rx <= barra.x + .15:
                if self.rx >= barra.x + .075 and self.vx < 0:
                    if abs(self.vx) < 0.25:
                        self.vx += barra.x + .075 - self.rx
                elif self.rx <= barra.x + .075 and self.vx > 0:
                    if abs(self.vx) < 0.25:
                        self.vx -= barra.x + .075 - self.rx
            else:
                self.bot = True
        if abs(self.ry + self.vy) + self.radius > 1.0:
            self.vy = -self.vy

        self.rx = self.rx + self.vx
        self.ry = self.ry + self.vy

    def increase_speed(self, vx, vy):
        if self.vx + vx >= 0: self.vx += vx
        if self.vy + vy >= 0: self.vy += vy

    def draw(self):
        stddraw.setPenColor(self.color)
        stddraw.filledCircle(self.rx, self.ry, self.radius)
