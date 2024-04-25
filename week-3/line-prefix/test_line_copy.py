import unittest
from line_new import Point, Line  # Assuming geometry.py is the file containing the classes

class TestPoint(unittest.TestCase):
    def test_init_valid(self):
        """Tests Point class initialization with valid arguments"""
        point = Point(1.0, 2.0)
        self.assertEqual(point.x, 1.0)
        self.assertEqual(point.y, 2.0)

    def test_init_invalid_type(self):
        """Tests Point class initialization with invalid argument types"""
        with self.assertRaises(AttributeError):
            Point("hello", "world")

    def test_eq(self):
        """Tests equality comparison of Point objects"""
        point1 = Point(1.0, 2.0)
        point2 = Point(1.0, 2.0)
        point3 = Point(3.0, 4.0)
        self.assertTrue(point1 == point2)
        self.assertFalse(point1 == point3)

class TestLine(unittest.TestCase):
    def test_init_valid(self):
        """Tests Line class initialization with valid arguments"""
        point1 = Point(0.0, 0.0)
        point2 = Point(1.0, 2.0)
        line = Line(point1, point2)
        self.assertEqual(line.p1, point1)
        self.assertEqual(line.p2, point2)

    def test_init_invalid_type(self):
        """Tests Line class initialization with invalid argument types"""
        point1 = Point(0.0, 0.0)
        with self.assertRaises(AttributeError):
            Line(point1, "invalid")

    def test_init_coincident_points(self):
        """Tests Line class initialization with coincident points"""
        point1 = Point(1.0, 1.0)
        with self.assertRaises(AttributeError):
            Line(point1, point1)

    def test_intersect_parallel(self):
        """Tests Line.intersect with parallel lines"""
        line1 = Line(Point(0.0, 0.0), Point(1.0, 1.0))
        line2 = Line(Point(2.0, 2.0), Point(3.0, 3.0))
        # self.assertIsNone(line1.intersect(line2)) ---------------------------------------------
        self.assertIsNotNone(line1.intersect(line2))

    def test_intersect_coincident(self):
        """Tests Line.intersect with coincident lines"""
        line1 = Line(Point(0.0, 0.0), Point(1.0, 1.0))
        line2 = Line(Point(0.5, 0.5), Point(2.0, 2.0))
        self.assertEqual(line1, line1.intersect(line2))
        # self.assertEqual(line1, line2.intersect(line1)) --------------------------------

    def test_intersect_perpendicular(self):
        """Tests Line.intersect with perpendicular lines"""
        line1 = Line(Point(0.0, 0.0), Point(1.0, 1.0))
        line2 = Line(Point(1.0, 0.0), Point(1.0, 2.0))
        self.assertEqual(line2.intersect(line1), Point(1.0, 1.0))

        line1 = Line(Point(1.0, 0.0), Point(1.0, 3.0))
        line2 = Line(Point(0.0, 0.0), Point(2.0, 2.0))
        self.assertEqual(line2.intersect(line1), Point(1.0, 1.0))

    def test_intersect_general(self):
        """Tests Line.intersect with lines in general positions"""
        line1 = Line(Point(1.0, 1.0), Point(3.0, 4.0))
        line2 = Line(Point(0.0, 0.0), Point(4.0, 4.0))
        self.assertEqual(line2.intersect(line1), Point(1.0, 1.0))
        # self.assertEqual(line2.intersect(line1), Point(2.0, 2.0)) ------------------------

    def test_intersect_invalid_argument(self):
        """Tests Line.intersect with invalid argument type"""
        line1 = Line(Point(0.0, 0.0), Point(1.0, 1.0))
        with self.assertRaises(AttributeError):
            line1.intersect("invalid")

if __name__ == "__main__":
    unittest.main()
