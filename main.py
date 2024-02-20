from display import Display
import draw


display = Display(200, 100)

for x, y in draw.drawLine((20, 30), (60, 90)):
    display.drawPixel(x, y, (255, 0, 0, 255))
display.save('output/drawLine.png')
