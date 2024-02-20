import os

from display import Display
import draw


width = 200
height = 100

display = Display(width, height)
p1 = (width // 3, height // 3)
p2 = (width * 2 // 3, height // 3)
p3 = (width // 2, height * 2 // 3)

for x, y in draw.drawFilledTriangle(p1, p2, p3):
    display.drawPixel(x, y, (255, 0, 0, 255))

os.makedirs('output', exist_ok=True)
display.save('output/drawTriangle.png')
