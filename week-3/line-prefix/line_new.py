"""a"""
from math import isnan

class Point:
    '''
    Клас для точок.
    '''

    def __init__(self, x: float, y: float) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise AttributeError
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__


class Line:
    '''
    Клас для прямих.
    '''

    def __init__(self, p1: 'Point', p2: 'Point') -> None:
        if not isinstance(p1, Point) or not isinstance(p2, Point) or p1 == p2:
            raise AttributeError
        self.p1 = p1
        self.p2 = p2

    def intersect(self, line2: 'Line') -> 'Point':
        """x"""
        if not isinstance(line2, Line):
            raise AttributeError

        k1 = (self.p2.y - self.p1.y
              ) / (self.p2.x - self.p1.x) if self.p2.x != self.p1.x else float('inf')
        k2 = (line2.p2.y - line2.p1.y) / (line2.p2.x -
                                          line2.p1.x) if line2.p2.x != line2.p1.x else float('inf')

        if k1 == k2:
            return self  # Lines are coincident
            # if self.p1.y - k1 * self.p1.x == line2.p1.y - k2 * line2.p1.x:
            #     return self  # Lines are coincident
            # return None

        if k1 == float('inf'):
            # Line 1 is vertical
            x = self.p1.x
            y = k2 * (x - line2.p1.x) + line2.p1.y
        elif k2 == float('inf'):
            # Line 2 is vertical
            x = line2.p1.x
            y = k1 * (x - self.p1.x) + self.p1.y
        else:
            # Regular case
            x = (k1 * self.p1.x - k2 * line2.p1.x +
                 line2.p1.y - self.p1.y) / (k1 - k2)
            y = k1 * (x - self.p1.x) + self.p1.y

        return Point(x if not isnan(x) else 0.0, y if not isnan(y) else 0.0)
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__
