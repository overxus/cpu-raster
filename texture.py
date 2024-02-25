import numpy as np
from PIL import Image


class Texture2d:
    def __init__(self, texture_path: str):
        img = Image.open(texture_path)
        self.width = img.width
        self.height = img.height
        self.textureData = np.array(img, dtype=np.uint8)

    def sample(self, x: float, y: float):
        """左下角为(0, 0), 右上角为(1, 1)"""
        x = min(max(0.0, x), 1.0)
        y = min(max(0.0, y), 1.0)
        tx = int((self.width - 1) * x)
        ty = int((self.height - 1) * (1 - y))
        return self.textureData[ty, tx]


if __name__ == '__main__':
    tex = Texture2d('images/cube.png')
    print(tex.textureData.shape)
