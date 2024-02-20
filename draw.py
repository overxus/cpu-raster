Point = tuple[int, int]


def drawLine(p1: Point, p2: Point) -> list[Point]:
    x1, y1 = p1
    x2, y2 = p2
    result = []

    if x1 == x2 and y1 == y2:
        result.append(p1)
    elif abs(y1 - y2) > abs(x1 - x2):
        m = (x2 - x1) / (y2 - y1)
        b = (y2 * x1 - y1 * x2) / (y2 - y1)
        for i in range(min(y1, y2), max(y1, y2) + 1):
            result.append((int(m * i + b), i))
    else:
        k = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - x1 * y2) / (x2 - x1)
        for i in range(min(x1, x2), max(x1, x2) + 1):
            result.append((i, int(k * i + b)))
    
    return result
