import os, math, time

from display import Display
from camera import Camera
import draw
from vec3 import vec3
from model import Model
import transform


def drawModel(model: Model, display: Display, camera: Camera):
    n_triangle = 0
    
    v_dict = {}
    for index, vertex in model.vertices_dict.items():
        v = vertex.copy()
        position = transform.rotate(vertex.position, vec3(1, 1, 1), time.time() * math.pi / 6)
        v.position = display.device2viewport(camera.projection(camera.view(position)))
        v_dict[index] = v

    for triangle_index_list in model.triangle_index_buffer:
        assert len(triangle_index_list) == 3
        idx1, idx2, idx3 = triangle_index_list
        v1, v2, v3 = v_dict[idx1], v_dict[idx2], v_dict[idx3]

        n_triangle += 1
        print('\rprocessing triangles: ', n_triangle, end='  ')
        draw.drawTriangle(display, v1, v2, v3)


if __name__ == '__main__':
    model = Model('models/cube.json')
    os.makedirs('output', exist_ok=True)

    display = Display(800, 600)
    camera = Camera(vec3(5, 5, 5), vec3(-5, -5, -5))

    while True:
        #camera.position = vec3(5 * math.cos(time.time() / 5), 5, 5 * math.sin(time.time() / 5))
        #camera.setLookAt(-camera.position)
        
        display.clearColorBuffer()
        display.clearDepthBuffer()
        drawModel(model, display, camera)
        display.save('output/drawTriangle.png')
