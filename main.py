import os
import numpy as np

from display import Display
import draw


def make_color(r: int, g: int, b: int, a: int = 255):
    return np.array((r, g, b, a), dtype=np.uint8)


width = 200
height = 100

display = Display(width, height)
p1 = (width // 3, height // 3)
c1 = make_color(255, 0, 0, 255)
p2 = (width * 2 // 3, height // 3)
c2 = make_color(0, 255, 0, 255)
p3 = (width // 2, height * 2 // 3)
c3 = make_color(0, 0, 255, 255)

draw.drawFilledTriangle(display, p1, c1, p2, c2, p3, c3)

os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
