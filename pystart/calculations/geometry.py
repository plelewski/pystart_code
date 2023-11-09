from math import pi, sqrt

def circle_are(r: float) -> float:
    return pi * r ** 2


def circle_circumference(r: float) -> float:
    return 2 * pi * r


def triangle_equilateral_circumference(a: float) -> float:
    return 3 * a


def middle_of_segment(x1: int, y1: int, x2: int, y2: int) -> tuple:
    return (x1 + x2) / 2, (y1 + y2) / 2


def segment_length(x1: int, y1: int, x2: int, y2: int) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
