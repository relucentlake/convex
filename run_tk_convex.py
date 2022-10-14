#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Triangle, Figure


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


def triangle_draw(self, tk):
    tk.draw_triangle(self.p, self.q, self.g)


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)
setattr(Triangle, 'draw', triangle_draw)

tk = TkDrawer()
f = Void()
tk.clean()

print("Заданный треугольник")
Figure.fixed_triangle = Triangle(R2Point(), R2Point(), R2Point())
Figure.fixed_triangle.draw(tk)

print("\nТочки плоскости")
f = Void()
try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        Figure.fixed_triangle.draw(tk)
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, g = {f.g()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
