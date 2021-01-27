import math


class Fraction:
    """This class provides a framework to work with fractions in python."""

    def __init__(self, numerator: int = 0, denominator: int = 1):
        """Creates a new fraction from two integers.

        :parameter numerator: (int) -- Numerator of the fraction (default 0).
        :parameter denominator: (int) -- Denominator of the fraction (default 1).

        If the denominator is negative,
        both the numerator and denominator will be negated to have a non-negative denominator.
        """
        if type(numerator) != int:
            raise TypeError(f"{numerator} is not an integer.")
        if type(denominator) != int:
            raise TypeError(f"{denominator} is not an integer.")
        if denominator == 0:
            raise ValueError("Denominators are not allowed to be zero.")

        if denominator < 0:
            self.n = -numerator
            self.d = -denominator
        elif denominator > 0:
            self.n = numerator
            self.d = denominator

    def __str__(self):
        """Handles how the fraction is represented as a string."""
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        return f"{self.n}/{self.d}"

    # The following section contains functions that handle arithmetic operations on fractions.
    # The core functionality is written first

    def __neg__(self):
        """Returns the arithmetic negative of the given fraction."""
        return Fraction(-self.n, self.d)

    def __add__(self, other):
        """Handles the addition of fractions with other fractions or integers"""
        frac = Fraction()

        if type(other) == int:  # Using the formula: a/x + b = (a +bx)/x
            frac.n = self.n + other * self.d
            frac.d = self.d

        elif type(other) == Fraction:

            if self.d == other.d:   # Using the formula: a/x + b/x = (a+b)/x
                frac.n = self.n + other.n
                frac.d = self.d
            else:   # Using the formula: a/x + b/y = (ay + bx)/xy
                frac.n = self.n * other.d + self.d * other.n
                frac.d = self.d * other.d

        else:
            raise TypeError("Addition can only be done with integers or other fractions.")

        return frac

    def __mul__(self, other):
        """Handles the multiplication of fractions with other fractions or integers."""
        frac = Fraction()

        if type(other) == Fraction:   # Using the formula: a/x * b/y = ab/xy
            frac.n = self.n * other.n
            frac.d = self.d * other.d

        elif type(other) == int:  # Using the formula: a/x * b = ab/x
            frac.n = self.n * other
            frac.d = self.d

        else:
            raise TypeError("Multiplication can only be done with integers or other fractions.")
        return frac

    def __truediv__(self, other):
        """Handles the division of fractions with integers and other fractions"""
        frac = Fraction()

        if type(other) == Fraction:    # Using the formula: (a/x) / (b/y) = ay/xb
            frac.n = self.n * other.d
            frac.d = self.d * other.n
        elif type(other) == int:    # Using the formula: (a/x) /b = a/xb
            frac.n = self.n
            frac.d = self.d * other
        else:
            raise TypeError("Division can only be done with integers or other fractions.")
        return frac

    # The following section has arithmetic functionality that depends on the core arithmetic functions.

    def __sub__(self, other):
        """Handles subtraction of fractions."""
        return self.__add__(-other)

    def __radd__(self, other):
        """Handles right side addition of fractions."""
        return self.__add__(other)

    def __rmul__(self, other):
        """Handles right side multiplication of fractions"""
        return self.__mul__(other)

    def __rsub__(self, other):
        """Handles the right side subtraction of fractions."""
        return self.__sub__(other)

    def __rtruediv__(self, other):
        """Handles right side division for fractions."""
        return self.__truediv__(other)

    # The following section has additional functionality to work on fractions.

    def fix_negative(self):
        """Negates both the numerator and denominator if the denominator is negative."""
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        return self

    def reciprocal(self):
        """Returns the reciprocal of the fraction it is called on as a new fraction.

        Does not modify the fraction it was called by.
        """
        return Fraction(self.d, self.n)

    def is_in_lowest_terms(self):
        """Checks if the fraction that is in lowest terms.
        :return True if the fraction is in lowest terms.
        :return False is the fraction is reducible further."""
        return math.gcd(self.n, self.d) == 1

    def is_reducible_by(self, factor: int):
        """Checks if the fraction can be reduced

        :parameter factor: the factor to possibility of reduction with.
        :return: True if fraction is reducible by the given factor. False otherwise
        """
        if type(factor) != int:
            raise TypeError(f"{factor} is not an integer.")

        if self.n % factor or self.d % factor:
            return False
        else:
            return True

    def reduce_by(self, factor: int):
        """Tries to reduce the fraction by a factor.

        :parameter factor: the factor to reduce the fraction by.

        If the fraction is reducible by the given factor.
        """
        if self.is_reducible_by(factor):
            self.n //= factor
            self.d //= factor
        return self

    def expand(self, factor: int):
        """Expands the fraction by a given multiplier."""
        if type(factor) != int:
            raise TypeError("Expansion of fractions is only allowed with integers.")
        self.n *= factor
        self.d *= factor
        return self

    def simplify(self):
        """Reduces the fraction to lowest terms if it isn't currently and fixes negative denominators."""
        self.fix_negative()
        return self.reduce_by(math.gcd(self.n, self.d))
