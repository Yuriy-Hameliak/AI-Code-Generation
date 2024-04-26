import unittest
from new import Polynomial, Quadratic
import coverage

class TestPolynomial(unittest.TestCase):

    def test_init_empty(self):
        p = Polynomial([])
        self.assertEqual(p.coeffs, [0])
        self.assertEqual(p.degree, 0)
    def test_init_single(self):
        p = Polynomial([0, 1])
        self.assertEqual(p.coeffs, [1])
        self.assertEqual(p.degree, 0)
    def test_init(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.coeffs, [3, 2, 1])
        self.assertEqual(p.degree, 2)
    def test_str(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(str(p), 'Polynomial: x**2+2x+3')
        p1 = Polynomial([1, 2, 0])
        self.assertEqual(str(p1), 'Polynomial: x**2+2x')
        p2 = Polynomial([1, 0, 3])
        self.assertEqual(str(p2), 'Polynomial: x**2+3')
        p3 = Polynomial([0, 0, 0])
        self.assertEqual(str(p3), 'Polynomial: 0')
    def test_repr(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(repr(p), 'Polynomial(coeffs=[1, 2, 3])')
        p1 = Polynomial([1, 2, 0])
        self.assertEqual(repr(p1), 'Polynomial(coeffs=[1, 2, 0])')
        p2 = Polynomial([1, 0, 3])
        self.assertEqual(repr(p2), 'Polynomial(coeffs=[1, 0, 3])')
        p3 = Polynomial([0, 0, 0])
        self.assertEqual(repr(p3), 'Polynomial(coeffs=[0])')
    def test_eq(self):
        p = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(p, p1)
        self.assertNotEqual(p, 1)
    def test_hash(self):
        p = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(hash(p), hash(p1))
    def test_add(self):
        p = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(p+p1, Polynomial([2, 4, 6]))
        self.assertIsNone(p1+1)
    def test_mul(self):
        p = Polynomial([1, 2, 3])
        p1 = Polynomial([1, 2, 3])
        self.assertEqual(p*p1, Polynomial([1, 4, 10, 12, 9]))
        self.assertIsNone(p1*1)
    def test_multiply_by_value(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.multiply_by_value(2), Polynomial([2, 4, 6]))
    def test_eval_at(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.eval_at(2), 11)
    def test_derivative(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p.derivative, Polynomial([2, 2]))


class TestQuadratic(unittest.TestCase):

    def test_init(self):
        p = Quadratic([1, 2, 3])
        self.assertEqual(p.coeffs, [3, 2, 1])
        self.assertEqual(p.degree, 2)
        self.assertEqual(p.a, 1)
        self.assertEqual(p.b, 2)
        self.assertEqual(p.c, 3)
        self.assertEqual(p.discriminant, -8)
    def test_init_error(self):
        with self.assertRaises(ValueError):
            p = Quadratic([0, 2, 3])
        with self.assertRaises(ValueError):
            p = Quadratic([1, 0, 3])
        with self.assertRaises(ValueError):
            p = Quadratic([1, 2, 3, 4])
    def test_repr(self):
        p = Quadratic([1, 2, 3])
        self.assertEqual(repr(p), 'Quadratic(a=1, b=2, c=3)')
    def test_str(self):
        p = Quadratic([1, 2, 3])
        self.assertEqual(str(p), 'Quadratic: x**2+2x+3')
    def test_number_of_real_roots(self):
        p = Quadratic([1, 2, 3])
        self.assertEqual(p.number_of_real_roots, 0)
        p1 = Quadratic([1, 2, -3])
        self.assertEqual(p1.number_of_real_roots, 2)
        p2 = Quadratic([1, 2, 1])
        self.assertEqual(p2.number_of_real_roots, 1)
    def test_get_real_roots(self):
        p = Quadratic([1, 2, 3])
        self.assertEqual(p.get_real_roots(), [])
        p1 = Quadratic([1, 2, -3])
        self.assertEqual(p1.get_real_roots(), [-3.0, 1.0])
        p2 = Quadratic([1, 2, 1])
        self.assertEqual(p2.get_real_roots(), [-1.0])

if __name__ == '__main__':
    unittest.main()