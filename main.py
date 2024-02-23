import os

from display import Display
from camera import Camera
import draw
from vec3 import vec3
from model import Model


width = 800
height = 600

display = Display(width, height)
camera = Camera(vec3(-3, 3, -3), vec3(1, -1, 1), vec3(0, 1, 0), view_width=1, view_height=1)


def canvas2Display(p: vec3) -> vec3:
    return vec3(int(width * (p.x + 1) / 2), int(height * (p.y + 1) / 2), p.z) 


def drawModel(model: Model, display: Display, camera: Camera):
    n_triangle = 0
    for triangle_index_list in model.triangle_index_buffer:
        assert len(triangle_index_list) == 3
        idx1, idx2, idx3 = triangle_index_list
        v1, v2, v3 = model.vertices_dict[idx1].copy(), model.vertices_dict[idx2].copy(), model.vertices_dict[idx3].copy()

        # print(v1.position, v2.position, v3.position)
        # print(camera.view(v1.position), camera.view(v2.position), camera.view(v3.position))

        v1.position = canvas2Display(camera.view(v1.position))
        v2.position = canvas2Display(camera.view(v2.position))
        v3.position = canvas2Display(camera.view(v3.position))

        n_triangle += 1
        print('\rprocessing triangles: ', n_triangle, end='')
        draw.drawTriangle(display, v1, v2, v3)


model = Model('models/cube.json')
drawModel(model, display, camera)

os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
