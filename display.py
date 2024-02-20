import numpy as np
from PIL import Image


class Display:
    def __init__(self, width: int, height: int):
        self.resize(width, height)
    
    @property
    def width(self):
        return self.__W
    
    @property
    def height(self):
        return self.__H

    def resize(self, width: int, height: int):
        self.__W = width
        self.__H = height
        self.__Data = np.zeros((self.__H, self.__W, 3), dtype=np.uint8)
    
    def save(self, image_path: str):
        """保存为图片"""
        image = Image.fromarray(self.__Data)
        image.save(image_path)

    def drawPixel(self, x: int, y: int, color):
        self.__Data[y, x] = color


if __name__ == '__main__':
    display = Display(400, 100)
    for i in range(100, 300):
        display.drawPixel(i, i // 4, (255, 0, 0))
    display.save('output/test.png')