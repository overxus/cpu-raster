import numpy as np
from vec3 import vec3


def make_color(r: int, g: int, b: int, a: int = 255):
    return np.array((r, g, b, a), dtype=np.uint8)


class Vertex3d:
    def __init__(self, position: vec3, color: list[int] = [255, 255, 255, 255]):
        self.position = position

        assert len(color) in (3, 4,)
        if len(color) == 3:
            color.append(255)
        self.color = make_color(*color)
