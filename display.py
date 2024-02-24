import numpy as np
from PIL import Image
from vec3 import vec3


class Display:
    def __init__(self, width: int, height: int):
        self.setViewport(width, height)
    
    def setViewport(self, width: int, height: int):
        """设置画布大小"""
        self.width, self.height = width, height
        self.colorBuffer = np.zeros((self.height, self.width, 4), dtype=np.uint8)
        self.depthBuffer = np.full((self.height, self.width), fill_value=np.inf, dtype=np.float32)

    def clearColorBuffer(self):
        self.colorBuffer = np.zeros((self.height, self.width, 4), dtype=np.uint8)

    def clearDepthBuffer(self):
        self.depthBuffer = np.full((self.height, self.width), fill_value=np.inf, dtype=np.float32)

    def drawPixel(self, x: int, y: int, z: float, color):
        """将(x, y)处的颜色color写入颜色缓冲中, z是这一点的深度"""
        if 0 <= x < self.width and 0 <= y < self.height:
            if z < self.depthBuffer[y, x]:
                self.colorBuffer[y, x] = color
                self.depthBuffer[y, x] = z

    def save(self, image_save_path: str):
        """保存画布为图片"""
        img = Image.fromarray(self.colorBuffer)
        img.save(image_save_path)

    def device2viewport(self, p: vec3) -> vec3:
        """p是x, y分量标准化为[-1, 1]的设备坐标"""
        vx = int(self.width * (p.x + 1) / 2)
        vy = int(self.height * (p.y + 1) / 2)
        return vec3(vx, vy, p.z)


if __name__ == '__main__':
    display = Display(400, 100)
    for i in range(100, 300):
        display.drawPixel(i, i // 4, 1.0, (255, 0, 0, 255))
    display.save('output/test.png')
