"""l"""
import unittest
from line_new import Point, Line

class TestLine(unittest.TestCase):
    """a"""

    def setUp(self) -> None:
        self.p1 = Point(1.0, 1.0)
        self.p2 = Point(5.0, 5.0)
        self.l1 = Line(self.p1, self.p2)
        self.l2 = Line(Point(0.0, 3.0), Point(3.0, 0.0))

    def test_init(self):
        """s"""
        self.assertRaises(ValueError,Line,Point(0.0,0.0),Point(0.0,0.0))
        self.assertEqual((self.p1.x, self.p1.y), (1.0, 1.0))
        self.assertEqual((self.p2.x, self.p2.y), (5.0, 5.0))
        self.assertEqual((self.l1.p1.x, self.l1.p2.x, self.l1.p1.y, self.l1.p2.y),
                         (self.p1.x, self.p2.x, self.p1.y, self.p2.y))
        self.assertEqual((self.l2.p1.x, self.l2.p2.x, self.l2.p1.y, self.l2.p2.y),
                         (0.0, 3.0, 3.0, 0.0))

    def test_intersect(self):
        """a"""
        self.assertEqual((self.l1.intersect(self.l2).x,
                         self.l1.intersect(self.l2).y), (1.5, 1.5))
        self.assertEqual(((l:=Line(Point(0.0, 0.0), Point(1.0, 1.0)
        ).intersect(Line(Point(0.0, 0.0), Point(2.0, 2.0)))).p1.x,l.p1.y),(0.0,0.0))
        self.assertEqual(((l:=Line(Point(0.0, 0.0), Point(1.0, 1.0)
        ).intersect(Line(Point(0.0, 0.0), Point(0.0, 2.0)))).x,l.y),(0.0,0.0))
        self.assertEqual(((l:=Line(Point(0.0, 0.0), Point(5.0, 8.0)
        ).intersect(Line(Point(3.0, -2.0), Point(0.0, 5.0)))).x,l.y),(1.3,2.0))
        self.assertEqual(Line(Point(0.0, 0.0), Point(1.0, 1.0)
                              ).intersect(Line(Point(0.0, -1.0), Point(1.0, 0.0))), None)
        self.assertEqual(Line(Point(0.0, 0.0), Point(5.0, 5.0)
                              ).intersect(Line(Point(0.0, -1.0), Point(1.0, 0.0))), None)

if __name__ == "__main__":
    unittest.main()
