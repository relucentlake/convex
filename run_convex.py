#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void, Triangle

print("Заданный треугольник")
Figure.fixed_triangle = Triangle(R2Point(), R2Point(), R2Point())

print("\nТочки плоскости")
f = Void()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, g = {f.g()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
