from deq import Deq
from r2point import R2Point
from math import sqrt


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def g(self):
        return 0


class Triangle:

    def __init__(self, p, q, g):
        self.p, self.q, self.g = p, q, g

    def inside(self, a):
        i = (self.q.x - self.p.x) * (a.y - self.p.y) - \
            (self.q.y - self.p.y) * (a.x - self.p.x)
        j = (self.g.x - self.q.x) * (a.y - self.q.y) - \
            (self.g.y - self.q.y) * (a.x - self.q.x)
        k = (self.p.x - self.g.x) * (a.y - self.g.y) - \
            (self.p.y - self.g.y) * (a.x - self.g.x)
        return (i > 0 and j > 0 and k > 0) or (i < 0 and j < 0 and k < 0)

    def border(self, a):
        i = (self.q.x - self.p.x) * (a.y - self.p.y) - \
            (self.q.y - self.p.y) * (a.x - self.p.x)
        j = (self.g.x - self.q.x) * (a.y - self.q.y) - \
            (self.g.y - self.q.y) * (a.x - self.q.x)
        k = (self.p.x - self.g.x) * (a.y - self.g.y) - \
            (self.p.y - self.g.y) * (a.x - self.g.x)
        return (i == 0 or j == 0 or k == 0) and \
            ((Triangle.length(a, self.p) + Triangle.length(a, self.q)
              == Triangle.length(self.q, self.p))
             or (Triangle.length(a, self.g)
             + Triangle.length(a, self.q) ==
             Triangle.length(self.q, self.g))
             or (Triangle.length(a, self.p)
             + Triangle.length(a, self.g) ==
             Triangle.length(self.g, self.p)))

    def is_inside(self, c, d):
        return ((self.inside(c) and self.inside(d))
                or (self.inside(c) and self.border(d)) or
                (self.inside(d) and self.border(c))) \
            or (self.border(c) and self.border(d) and
                (Triangle.is_intersect(c, d, self.p, self.q)
                 or Triangle.is_intersect(c, d, self.g, self.q) or
                 Triangle.is_intersect(c, d, self.p, self.g)))

    def is_border(self, c, d):
        return self.border(c) and self.border(d) and \
            not (Triangle.is_intersect(c, d, self.p, self.q)
                 or Triangle.is_intersect(c, d, self.g, self.q) or
                 Triangle.is_intersect(c, d, self.p, self.g))

    def is_equal_1(self, a):
        return a.x == self.p.x and a.y == self.p.y

    def is_equal_2(self, a):
        return a.x == self.q.x and a.y == self.q.y

    def is_equal_3(self, a):
        return a.x == self.g.x and a.y == self.g.y

    @staticmethod
    def is_intersect(a, b, c, d):
        return (R2Point.cross(a, c, a, b) * R2Point.cross(a, d, a, b) < 0 and
                R2Point.cross(c, a, c, d) * R2Point.cross(c, b, c, d) <= 0) \
            or (R2Point.cross(a, c, a, b) * R2Point.cross(a, d, a, b) <= 0 and
                R2Point.cross(c, a, c, d) * R2Point.cross(c, b, c, d) < 0)

    def intersection1(self, a, b):
        if Triangle.is_intersect(a, b, self.q, self.g):
            return R2Point(((a.x * b.y - b.x * a.y) * (self.q.x - self.g.x)
                            - (a.x - b.x) * (
                self.q.x * self.g.y - self.q.y * self.g.x)) /
                ((a.x - b.x) * (self.q.y - self.g.y) -
                 (a.y - b.y) * (self.q.x - self.g.x)),
                ((a.x * b.y - b.x * a.y) * (self.q.y - self.g.y)
                 - (a.y - b.y) * (
                    self.q.x * self.g.y - self.q.y * self.g.x)) /
                ((a.x - b.x) * (self.q.y - self.g.y) - (a.y - b.y)
                 * (self.q.x - self.g.x)))

    def intersection2(self, a, b):
        if Triangle.is_intersect(a, b, self.p, self.q):
            return R2Point(((a.x * b.y - b.x * a.y) * (self.q.x - self.p.x)
                            - (a.x - b.x) * (
                self.q.x * self.p.y - self.q.y * self.p.x)) /
                ((a.x - b.x) * (self.q.y - self.p.y) -
                 (a.y - b.y) * (self.q.x - self.p.x)),
                ((a.x * b.y - b.x * a.y) * (self.q.y - self.p.y)
                 - (a.y - b.y) * (
                    self.q.x * self.p.y - self.q.y * self.p.x)) /
                ((a.x - b.x) * (self.q.y - self.p.y) - (a.y - b.y)
                 * (self.q.x - self.p.x)))

    def intersection3(self, a, b):
        if Triangle.is_intersect(a, b, self.p, self.g):
            return R2Point(((a.x * b.y - b.x * a.y) * (self.p.x - self.g.x)
                            - (a.x - b.x) * (
                self.p.x * self.g.y - self.p.y * self.g.x)) /
                ((a.x - b.x) * (self.p.y - self.g.y) -
                 (a.y - b.y) * (self.p.x - self.g.x)),
                ((a.x * b.y - b.x * a.y) * (self.p.y - self.g.y)
                 - (a.y - b.y) * (
                    self.p.x * self.g.y - self.p.y * self.g.x)) /
                ((a.x - b.x) * (self.p.y - self.g.y) - (a.y - b.y)
                 * (self.p.x - self.g.x)))

    @staticmethod
    def length(a, b):
        if isinstance(a, R2Point) and isinstance(b, R2Point):
            return sqrt(((a.x - b.x)**2 + (a.y - b.y)**2))
        else:
            return 0

    def is_convex(self, a, b):
        return (Triangle.is_intersect(a, b, self.p, self.q) and
                Triangle.is_intersect(a, b, self.p, self.g)) or \
            (Triangle.is_intersect(a, b, self.p, self.q) and
             Triangle.is_intersect(a, b, self.q, self.g)) or \
            (Triangle.is_intersect(a, b, self.p, self.g) and
             Triangle.is_intersect(a, b, self.q, self.g))

    def inside_length(self, a, b):
        if self.inside(a) and not (self.is_convex(a, b)):
            return Triangle.length(self.intersection1(a, b), a) \
                + Triangle.length(self.intersection2(a, b), a) \
                + Triangle.length(self.intersection3(a, b), a)
        elif self.inside(b) and not (self.is_convex(a, b)):
            return Triangle.length(self.intersection1(a, b), b) \
                + Triangle.length(self.intersection2(a, b), b) \
                + Triangle.length(self.intersection3(a, b), b)
        elif self.inside(a) and self.is_convex(a, b):
            return (Triangle.length(self.intersection1(a, b), a)
                    + Triangle.length(self.intersection2(a, b), a)
                    + Triangle.length(self.intersection3(a, a), b))/2
        elif self.inside(b) and self.is_convex(a, b):
            return (Triangle.length(self.intersection1(a, b), b)
                    + Triangle.length(self.intersection2(a, b), b)
                    + Triangle.length(self.intersection3(a, b), b))/2
        elif Triangle.is_intersect(a, b, self.p, self.q) and \
                Triangle.is_intersect(a, b, self.g, self.q) and \
        Triangle.is_intersect(a, b, self.g, self.p):
            return (Triangle.length(self.intersection1(a, b),
                                    self.intersection2(a, b))
                    + Triangle.length(self.intersection2(a, b),
                                      self.intersection3(a, b))
                    + Triangle.length(self.intersection3(a, b),
                                      self.intersection1(a, b)))/2
        elif self.is_equal_1(a) or self.is_equal_1(b) and \
                Triangle.is_intersect(a, b, self.g, self.q):
            return Triangle.length(a, self.intersection1(a, b))
        elif self.is_equal_2(a) or self.is_equal_2(b) and \
                Triangle.is_intersect(a, b, self.g, self.p):
            return Triangle.length(a, self.intersection3(a, b))
        elif self.is_equal_3(a) or self.is_equal_3(b) and \
                Triangle.is_intersect(a, b, self.g, self.q):
            return Triangle.length(a, self.intersection2(a, b))
        else:
            return Triangle.length(self.intersection1(a, b),
                                   self.intersection2(a, b)) \
                + Triangle.length(self.intersection2(a, b),
                                  self.intersection3(a, b)) \
                + Triangle.length(self.intersection3(a, b),
                                  self.intersection1(a, b))


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return self

    def g(self):
        if self.fixed_triangle.is_inside(self.p, self.q):
            return Triangle.length(self.p, self.q)

        elif self.fixed_triangle.is_border(self.p, self.q):
            return 0

        else:
            return self.fixed_triangle.inside_length(self.p, self.q)


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._g = 0

        if self.fixed_triangle.is_inside(a, b):
            self._g += Triangle.length(a, b)
        else:
            self._g += self.fixed_triangle.inside_length(a, b)

        if self.fixed_triangle.is_inside(a, c):
            self._g += Triangle.length(a, c)
        else:
            self._g += self.fixed_triangle.inside_length(a, c)

        if self.fixed_triangle.is_inside(c, b):
            self._g += Triangle.length(c, b)
        else:
            self._g += self.fixed_triangle.inside_length(c, b)

    def g(self):
        return self._g

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            if self.fixed_triangle.is_inside(self.points.first(),
                                             self.points.last()):
                self._g -= Triangle.length(self.points.first(),
                                           self.points.last())
            else:
                self._g -= self.fixed_triangle.inside_length(
                    self.points.first(), self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                if self.fixed_triangle.is_inside(p, self.points.first()):
                    self._g -= Triangle.length(p, self.points.first())
                else:
                    self._g -= self.fixed_triangle.inside_length(
                        p, self.points.first())
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                if self.fixed_triangle.is_inside(p, self.points.last()):
                    self._g -= Triangle.length(p, self.points.last())
                else:
                    self._g -= self.fixed_triangle.inside_length(
                        p, self.points.last())
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            if self.fixed_triangle.is_inside(t, self.points.first()) \
                    and self.fixed_triangle.is_inside(t, self.points.last()):
                self._g += Triangle.length(t, self.points.first()) + \
                    Triangle.length(t, self.points.last())
            elif self.fixed_triangle.is_inside(t, self.points.first()):
                self._g += Triangle.length(t, self.points.first()) + \
                    self.fixed_triangle.inside_length(t, self.points.last())
            elif self.fixed_triangle.is_inside(t, self.points.last()):
                self._g += Triangle.length(t, self.points.last()) + \
                    self.fixed_triangle.inside_length(t, self.points.first())
            else:
                self._g += \
                    self.fixed_triangle.inside_length(t,
                                                      self.points.last(
                                                      )) + \
                    self.fixed_triangle.inside_length(t, self.points.first())
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
