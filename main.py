import os
import numpy as np

from display import Display
from camera import Camera
import draw
from vec3 import vec3


def make_color(r: int, g: int, b: int, a: int = 255):
    return np.array((r, g, b, a), dtype=np.uint8)

R = make_color(255, 0, 0)
G = make_color(0, 255, 0)
B = make_color(0, 0, 255)


width = 200
height = 100

display = Display(width, height)
camera = Camera(vec3(0, 0, 0), vec3(0, 0, 1), vec3(0, 1, 0))



def ViewToCanvas(px, py, pz):
    d = 1
    cx, cy = d * px / pz, d * py / pz
    return int((cx + d) * width // (2 * d)), int((cy + d) * height // (2 * d))

p1 = vec3(0.0, 0.0, 1.0)
p2 = vec3(-0.5, 0.5, 1.0)
p3 = vec3(0.0, 0.5, 2.0)

def canvas2Display(p):
    x, y = p
    return int(width * (x + 1) / 2), int(height * (y + 1) / 2) 

draw.drawFilledTriangle(
    display,
    canvas2Display(camera.point2canvas(p1)),
    R,
    canvas2Display(camera.point2canvas(p2)),
    G,
    canvas2Display(camera.point2canvas(p3)),
    B
)


os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
