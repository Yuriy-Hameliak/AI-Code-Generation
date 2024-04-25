"""s"""


class Point:
    """s"""

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    """a"""

    def __init__(self, p1, p2) -> None:
        if p1.x==p2.x and p1.y==p2.y:
            raise ValueError
        self.p1 = p1
        self.p2 = p2

    def intersect(self, line2):
        """s"""
        denominator = (self.p1.x - self.p2.x) * (line2.p1.y - line2.p2.y
            ) - (self.p1.y - self.p2.y) * (line2.p1.x - line2.p2.x)
        if denominator == 0:
            if (self.p2.x - self.p1.x) * (line2.p1.y - self.p1.y) == (line2.p1.x - self.p1.x
            ) * (self.p2.y - self.p1.y) and (self.p2.x - self.p1.x) * (line2.p2.y - self.p1.y
            ) == (line2.p2.x - self.p1.x) * (self.p2.y - self.p1.y):
                return self
            return None
        x = ((self.p1.x * self.p2.y - self.p1.y * self.p2.x) * (line2.p1.x - line2.p2.x
        ) - (self.p1.x - self.p2.x) * (line2.p1.x * line2.p2.y - line2.p1.y*line2.p2.x))/denominator
        y = ((self.p1.x * self.p2.y - self.p1.y * self.p2.x) * (line2.p1.y - line2.p2.y
        ) - (self.p1.y - self.p2.y) * (line2.p1.x * line2.p2.y - line2.p1.y*line2.p2.x))/denominator
        return Point(round(x,1),round(y,1))
