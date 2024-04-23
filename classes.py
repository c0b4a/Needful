#!/usr/bin/env python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self = (x, y)

example: Point = (0,12)

print(example)