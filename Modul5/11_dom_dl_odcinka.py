from math import sqrt

def calculate_segment_length(start: tuple, end: tuple) -> float:
    x1, y1 = start
    x2, y2 = end

    return sqrt((x2-x1)**2 + (y2-y1)**2)

length = calculate_segment_length(
    (0, 0),
    (0, 4)
)

print(length)
