import os
import numpy as np

from display import Display
from camera import Camera
import draw
from vec3 import vec3
from model import Model


def make_color(r: int, g: int, b: int, a: int = 255):
    return np.array((r, g, b, a), dtype=np.uint8)

R = make_color(255, 0, 0)
G = make_color(0, 255, 0)
B = make_color(0, 0, 255)


width = 200
height = 100

display = Display(width, height)
camera = Camera(vec3(0, 0, -10), vec3(0, 0, 1), vec3(0, 1, 0))


def canvas2Display(p):
    x, y = p
    return int(width * (x + 1) / 2), int(height * (y + 1) / 2) 


def drawModel(model: Model, display: Display, camera: Camera):
    for triangle_index_list in model.triangle_index_buffer:
        assert len(triangle_index_list) == 3
        idx1, idx2, idx3 = triangle_index_list
        v1, v2, v3 = model.vertices_dict[idx1], model.vertices_dict[idx2], model.vertices_dict[idx3]
        
        draw.drawFilledTriangle(
            display,
            canvas2Display(camera.point2canvas(v1.position)), v1.color,
            canvas2Display(camera.point2canvas(v2.position)), v2.color,
            canvas2Display(camera.point2canvas(v3.position)), v3.color)

# p1 = vec3(0.0, 0.0, 1.0)
# p2 = vec3(-0.5, 0.5, 1.0)
# p3 = vec3(0.0, 0.5, 2.0)


# draw.drawFilledTriangle(
#     display,
#     canvas2Display(camera.point2canvas(p1)),
#     R,
#     canvas2Display(camera.point2canvas(p2)),
#     G,
#     canvas2Display(camera.point2canvas(p3)),
#     B
# )

model = Model('models/cube.json')
drawModel(model, display, camera)

os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
