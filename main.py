import os
import numpy as np

from display import Display
import draw


def make_color(r: int, g: int, b: int, a: int = 255):
    return np.array((r, g, b, a), dtype=np.uint8)


width = 200
height = 100

display = Display(width, height)

# p1 = (width // 3, height // 3)
# c1 = make_color(255, 0, 0, 255)
# p2 = (width * 2 // 3, height // 3)
# c2 = make_color(0, 255, 0, 255)
# p3 = (width // 2, height * 2 // 3)
# c3 = make_color(0, 0, 255, 255)

# draw.drawFilledTriangle(display, p1, c1, p2, c2, p3, c3)

R = make_color(255, 0, 0)
G = make_color(0, 255, 0)
B = make_color(0, 0, 255)

def ViewToCanvas(px, py, pz):
    d = 1
    cx, cy = d * px / pz, d * py / pz
    return int((cx + d) * width // (2 * d)), int((cy + d) * height // (2 * d))

p1 = ViewToCanvas(1, 1, 1.5)
p2 = ViewToCanvas(1, -1, 1.5)
p3 = ViewToCanvas(-1, -1, 1.5)
p4 = ViewToCanvas(-1, 1, 1.5)
p5 = ViewToCanvas(1, 1, 2)
p6 = ViewToCanvas(1, -1, 2)
p7 = ViewToCanvas(-1, -1, 2)
p8 = ViewToCanvas(-1, 1, 2)


draw.drawLine(display, p1, R, p2, R)
draw.drawLine(display, p2, R, p3, R)
draw.drawLine(display, p3, R, p4, R)
draw.drawLine(display, p4, R, p1, R)

draw.drawLine(display, p5, G, p6, G)
draw.drawLine(display, p6, G, p7, G)
draw.drawLine(display, p7, G, p8, G)
draw.drawLine(display, p8, G, p5, G)

draw.drawLine(display, p1, B, p5, B)
draw.drawLine(display, p2, B, p6, B)
draw.drawLine(display, p3, B, p7, B)
draw.drawLine(display, p4, B, p8, B)

os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
