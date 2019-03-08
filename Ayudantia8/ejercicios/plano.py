class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        base = self.p2.x - self.p1.x  # x2 - x1 = base
        altura = self.p2.y - self.p1.y  # y2 - y1 = altura
        return int(base * altura)

    def points(self):
        p = []
        for x in range(self.p1.x, self.p2.x + 1):
            for y in range(self.p1.y, self.p2.y + 1):
                p.append(Point(x, y))
        return list(p)

    def solapado(self, rectangle):
        for p1 in self.points():
            for p2 in rectangle.points():
                if p1 == p2:
                    return True
        return False

    def interseccion(self, rectangle):
        if not self.solapado(rectangle):
            raise ValueError('({}) y ({}) no están solapados'.format(self, rectangle))
        x = []
        y = []
        for p in self.points():
            for p1 in rectangle.points():
                if p == p1:
                    x.append(p.x)
                    y.append(p.y)
        x.sort()
        y.sort()
        return Rectangle(Point(x[0], y[0]), Point(x[len(x) - 1], y[len(y) - 1]))

    def __str__(self):
        return 'p1: ({}, {}) p2: ({}, {})'.format(self.p1.x, self.p1.y, self.p2.x, self.p2.y)


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False
