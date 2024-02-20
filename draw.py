Point = tuple[int, int]


def interval(x1: int, x2: int):
    if x1 < x2:
        yield from range(x1, x2 + 1)
    else:
        yield from range(x1, x2 - 1, -1)


def interpolate(x1: int, y1: float, x2: int, y2: float):
    """线性插值，从(x1, y1)线性插值到(x2, y2), 不过假设y1和y2都是浮点数"""
    if x1 == x2:
        return [y1]
    
    k = (y2 - y1) / (x2 - x1)
    if x2 < x1:
        k = -k
    y = y1

    result = []
    for _ in interval(x1, x2):
        result.append(y)
        y += k
    return result


def drawLine(p1: Point, p2: Point) -> list[Point]:
    x1, y1 = p1
    x2, y2 = p2

    if abs(y1 - y2) > abs(x1 - x2):
        return [(int(x), y) for x, y in zip(interpolate(y1, x1, y2, x2), interval(y1, y2))]
    else:
        return [(x, int(y)) for x, y in zip(interval(x1, x2), interpolate(x1, y1, x2, y2))]


def drawTriangle(p1: Point, p2: Point, p3: Point) -> list[Point]:
    result = drawLine(p1, p2)
    result += drawLine(p2, p3)
    result += drawLine(p1, p3)
    return result


def drawFilledTriangle(p1: Point, p2: Point, p3: Point) -> list[Point]:
    """绘制填充的三角形"""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    if y1 > y2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    if y1 > y3:
        x1, x3 = x3, x1
        y1, y3 = y3, y1
    if y2 > y3:
        x2, x3 = x3, x2
        y2, y3 = y3, y2
    
    x13 = interpolate(y1, x1, y3, x3)
    x12 = interpolate(y1, x1, y2, x2)
    x23 = interpolate(y2, x2, y3, x3)
    x12.pop()
    x123 = x12 + x23

    result = []
    for idx, y in enumerate(interval(y1, y3)):
        for x in interval(int(x123[idx]), int(x13[idx])):
            result.append((x, y))
    return result
