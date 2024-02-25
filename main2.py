import os, time, math

from vec3 import vec3
from vertex import Vertex3d
from display import Display
from camera import Camera
from texture import Texture2d
import transform, draw


planeData = [
    [-1, -1, 0, 0, 0],
    [-1, 1, 0, 0, 1],
    [1, -1, 0, 1, 0],
    [-1, 1, 0, 0, 1],
    [1, -1, 0, 1, 0],
    [1, 1, 0, 1, 1]
]

def drawModel(vs: list[Vertex3d], display: Display, camera: Camera, texture: Texture2d):
    vertexList = []
    for vertex in vs:
        v = vertex.copy()
        position = transform.rotate(vertex.position, vec3(0, 1, 0), time.time() * math.pi / 8)
        v.position = display.device2viewport(camera.projection(camera.view(position)))
        vertexList.append(v)

    # n_triangle = 0
    for i in range(len(vertexList) // 3):
        v1, v2, v3 = vertexList[3 * i], vertexList[3 * i + 1], vertexList[3 * i + 2]
        # n_triangle += 1
        # print('\rprocessing triangles: ', n_triangle, end='  ')
        draw.drawTexTriangle(display, v1, v2, v3, texture)


if __name__ == '__main__':
    os.makedirs('output', exist_ok=True)

    vertexList = []
    for px, py, pz, ux, uy in planeData:
        vertex = Vertex3d(position=vec3(px, py, pz), texCoord=[ux, uy])
        vertexList.append(vertex)

    display = Display(800, 600)
    camera = Camera(vec3(0, 0, -3), vec3(0, 0, 1))
    texture = Texture2d('output/tex.png')

    last_time = time.time()

    n_frame = 0
    while True:
        display.clearColorBuffer()
        display.clearDepthBuffer()
        drawModel(vertexList, display, camera, texture)
        display.save('output/drawTriangle.png')

        n_frame += 1
        print('\rdraw frame: ', n_frame, end='   ')

        # delta = time.time() - last_time
        # if delta < 2.0:
        #     time.sleep(2.0 - delta)
        #     last_time = time.time()
