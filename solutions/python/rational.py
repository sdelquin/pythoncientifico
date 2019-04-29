class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    @staticmethod
    def _mcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def _simplify(self, in_place=True):
        mcd = Rational._mcd(self.numerator, self.denominator)
        new_numerator = self.numerator / mcd
        new_denominator = self.denominator / mcd
        if in_place:
            self.numerator = new_numerator
            self.denominator = new_denominator
        else:
            return Rational(new_numerator, new_denominator)

    @property
    def value(self):
        return self.numerator / self.denominator

    def __abs__(self):
        return Rational(abs(self.numerator), abs(self.denominator))

    def __add__(self, other):
        new_numerator = self.numerator * self.denominator + \
            other.denominator * self.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * self.denominator - \
            other.denominator * self.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __div__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def pow(self, x):
        new_numerator = self.numerator ** x
        new_denominator = self.denominator ** x
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator * other.denominator == \
            other.numerator * self.denominator
