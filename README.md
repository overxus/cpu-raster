# 基于Python的软光栅实现

## 1. 实现画布类Display
它表示绘制颜色的画布，本质上是一个数组，可以向数组的特定位置写入颜色。
```python
drawPixel(x: int, y: int, color)  # 向(x, y)处写入颜色color
```

## 2. 绘制线段
给定两点坐标(x1, y1)和(x2, y2), 绘制一条线段。

## 3. 绘制并填充三角形
绘制三角形，其实就是绘制三条线段，非常简单；
填充三角形，可以将三角形的顶点按照X(Y)方向排序，填充的三小型可以看作一系列竖直(水平)的线段。
