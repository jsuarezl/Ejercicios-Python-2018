class Rational:
    def __init__(self, n, m):
        self.n = int(n)
        self.m = int(m)
        pass

    def plus(self, rational):
        if self.m == rational.m:
            return Rational(self.n + rational.n, self.m)
        else:
            A = max(self.m, rational.m)
            mcd = B = min(self.m, rational.m)
            while B:
                mcd = B
                B = A % B
                A = mcd
            mcm = (self.m * rational.m) // mcd
            return Rational(self.n * (self.m / mcm) + rational.n * (rational.n / mcm), mcm)

    def minus(self, rational):
        if self.m == rational.m:
            return Rational(self.n - rational.n, self.m)
        else:
            return Rational(self.n * rational.m - rational.n * self.m, self.m * rational.m)

    def times(self, rational):
        return Rational(self.n * rational.n, self.m * rational.m)

    def divides(self, rational):
        return Rational(self.n * rational.m, self.m * rational.n)

    def __str__(self):
        self.value()
        return str('{}/{}').format(self.n, self.m)

    def value(self):
        if self.n == 0:
            raise ValueError('El numerador es 0, no se puede realizar la operación')
        elif self.m == 0:
            raise ValueError('El denomiador es 0, no se puede realizar la operación')
        return float(self.n / self.m)
