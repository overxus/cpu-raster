from display import Display
from vertex import Vertex3d


Point = tuple[int, int]
Color = tuple[int, int, int, int]


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


def drawLine(display: Display, p1, color1, p2, color2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        for y, alpha in zip(interval(y1, y2), interpolate(y1, 1.0, y2, 0.0)):
            display.drawPixel(x1, y, alpha * color1 + (1 - alpha) * color2)
    elif y1 == y2:
        for x, alpha in zip(interval(x1, x2), interpolate(x1, 1.0, x2, 0.0)):
            display.drawPixel(x, y1, alpha * color1 + (1 - alpha) * color2)
    elif abs(y1 - y2) > abs(x1 - x2):
        for x, y, alpha in zip(interpolate(y1, x1, y2, x2), interval(y1, y2), interpolate(y1, 1.0, y2, 0.0)):
            color = alpha * color1 + (1 - alpha) * color2
            display.drawPixel(int(x), y, color)
    else:
        for x, y, alpha in zip(interval(x1, x2), interpolate(x1, y1, x2, y2), interpolate(x1, 1.0, x2, 0.0)):
            color = alpha * color1 + (1 - alpha) * color2
            display.drawPixel(x, int(y), color)


def drawTriangle(display: Display, v1: Vertex3d, v2: Vertex3d, v3: Vertex3d):
    if v1.position.y > v2.position.y:
        v1, v2 = v2, v1
    if v1.position.y > v3.position.y:
        v1, v3 = v3, v1
    if v2.position.y > v3.position.y:
        v2, v3 = v3, v2
    
    x1, y1 = int(v1.position.x), int(v1.position.y)
    x2, y2 = int(v2.position.x), int(v2.position.y)
    x3, y3 = int(v3.position.x), int(v3.position.y)

    x13 = interpolate(y1, x1, y3, x3)
    c13 = [alpha * v1.color + (1 - alpha) * v3.color for alpha in interpolate(y1, 1.0, y3, 0.0)]
    z13_inv = [alpha * 1 / v1.position.z + (1 - alpha) * 1 / v3.position.z for alpha in interpolate(y1, 1.0, y3, 0.0)]

    x12 = interpolate(y1, x1, y2, x2)
    c12 = [alpha * v1.color + (1 - alpha) * v2.color for alpha in interpolate(y1, 1.0, y2, 0.0)]
    z12_inv = [alpha * 1 / v1.position.z + (1 - alpha) * 1 / v2.position.z for alpha in interpolate(y1, 1.0, y2, 0.0)]

    x23 = interpolate(y2, x2, y3, x3)
    c23 = [alpha * v2.color + (1 - alpha) * v3.color for alpha in interpolate(y2, 1.0, y3, 0.0)]
    z23_inv = [alpha * 1 / v2.position.z + (1 - alpha) * 1 / v3.position.z for alpha in interpolate(y2, 1.0, y3, 0.0)]

    x12.pop()
    c12.pop()
    z12_inv.pop()

    x123 = x12 + x23
    c123 = c12 + c23
    z123_inv = z12_inv + z23_inv

    for idx, y in enumerate(interval(y1, y3)):
        px1, px2 = int(x123[idx]), int(x13[idx])
        cx1, cx2 = c123[idx], c13[idx]
        zx1, zx2 = 1 / z123_inv[idx], 1 / z13_inv[idx]

        for x, alpha in zip(interval(px1, px2), interpolate(px1, 1.0, px2, 0.0)):
            color = alpha * cx1 + (1 - alpha) * cx2
            z = alpha * zx1 + (1 - alpha) * zx2
            display.drawPixel(x, y, z, color)


"""
def drawFilledTriangle(display: Display, p1, color1, p2, color2, p3, color3):
    # 绘制填充的三角形
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
    c13 = [alpha * color1 + (1 - alpha) * color3 for alpha in interpolate(y1, 1.0, y3, 0.0)]
    x12 = interpolate(y1, x1, y2, x2)
    c12 = [alpha * color1 + (1 - alpha) * color2 for alpha in interpolate(y1, 1.0, y2, 0.0)]
    x23 = interpolate(y2, x2, y3, x3)
    c23 = [alpha * color2 + (1 - alpha) * color3 for alpha in interpolate(y2, 1.0, y3, 0.0)]
    x12.pop()
    c12.pop()
    x123 = x12 + x23
    c123 = c12 + c23

    for idx, y in enumerate(interval(y1, y3)):
        px1, px2 = int(x123[idx]), int(x13[idx])
        cx1, cx2 = c123[idx], c13[idx]
        drawLine(display, (px1, y), cx1, (px2, y), cx2) 
"""