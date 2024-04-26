import math


"""Polynomial"""
class Polynomial:
    """class Polynomial"""
    def __init__(self, coefs: list|tuple) -> None:
        """Construct a polynomial from its coefficients."""
        degree = len(coefs)-1
        coef = list(coefs[:])
        for i in coefs:
            if i == 0:
                coef.pop(0)
                degree -= 1
            else:
                break
        self.degree = degree if degree > 0 else 0
        self.coeffs = coef[::-1] if coef else [0]

    def __str__(self) -> str:
        """Returns a string representation of the polynomial."""
        if self.coeffs == [0]:
            return "Polynomial: 0"
        res = "Polynomial: "
        degree = self.degree
        for coef in self.coeffs[::-1]:
            if coef == 0:
                degree -= 1
                continue
            res += f"{'-' if coef < 0 else '+' if degree != self.degree else ''}\
{abs(coef) if coef not in [-1, 1] else '' if degree >0 else abs(coef)}\
{'x**'+str(degree) if degree not in [0, 1] else 'x' if degree == 1 else ''}"
            degree -= 1
        return res

    def __repr__(self) -> str:
        """Return a string representation of the polynomial."""
        return f"Polynomial(coeffs={self.coeffs[::-1]})"

    def __eq__(self, other):
        """Returns True if two polynomials are equal, False otherwise."""
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        return self.coeffs == [other]

    def __hash__(self) -> int:
        """hash function for the Polynomial class."""
        return hash(sum([self.coeffs[0], self.coeffs[-1], self.degree]))

    def __add__(self, other):
        """Add two polynomials together and return a new polynomial."""
        if isinstance(other, Polynomial):
            degree = max(self.degree, other.degree)
            return Polynomial([other.coeffs[i]+self.coeffs[i] for i in range(degree+1)][::-1])
        return None

    def __mul__(self, other):
        """Multiply two polynomials together and return a new polynomial."""
        if isinstance(other, Polynomial):
            _s = self.coeffs
            _v = other.coeffs
            res = [0]*(len(_s)+len(_v)-1)
            for selfpow,selfco in enumerate(_s):
                for valpow,valco in enumerate(_v):
                    res[selfpow+valpow] += selfco*valco
            return Polynomial(res[::-1])
        return None

    def multiply_by_value(self, value):
        """Multiply all coefficients by the given value and return a new polynomial."""
        return Polynomial([i*value for i in self.coeffs][::-1])

    def eval_at(self, x):
        """Evaluates the polynomial at the given value of x."""
        res = 0
        for i, coef in enumerate(self.coeffs):
            res += coef * (x ** i)
        return res

    @property
    def derivative(self):
        """Returns the derivative of the polynomial."""
        return Polynomial([self.coeffs[i]*i for i in range(1, len(self.coeffs))][::-1])

class Quadratic(Polynomial):
    """A quadratic polynomial class."""
    def __init__(self, coefs: list|tuple) -> None:
        """Construct a quadratic polynomial from its coefficients."""
        if len(coefs) != 3 or coefs[0] == 0 or coefs[1] == 0:
            raise ValueError("Quadratic polynomial must have exactly 3 coefficients")
        super().__init__(coefs)
        self.degree = 2
        self.a = coefs[0]
        self.b = coefs[1]
        self.c = coefs[2]
        self.discriminant = self.b**2 - 4*self.a*self.c

    def __repr__(self) -> str:
        """Returns a string representation of the quadratic equation."""
        return f'Quadratic(a={self.a}, b={self.b}, c={self.c})'

    def __str__(self) -> str:
        """Returns a string representation of the quadratic equation."""
        return super().__str__().replace("Polynomial", "Quadratic")

    @property
    def number_of_real_roots(self):
        """Number of real roots of the quadratic equation."""
        return 2 if self.discriminant > 0 else 1 if self.discriminant == 0 else 0

    def get_real_roots(self):
        """Returns the real roots of the quadratic, if any."""
        if self.number_of_real_roots == 0:
            return []
        if self.number_of_real_roots == 1:
            return [-self.b/(2*self.a)]
        root1 = (-self.b + (self.discriminant)**0.5)/(2*self.a)
        root2 = (-self.b - (self.discriminant)**0.5)/(2*self.a)
        return [min(root1, root2), max(root1, root2)]
