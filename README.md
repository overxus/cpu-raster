# 基于Python的软光栅实现
## 1. 实现画布类Display
它表示绘制颜色的画布，本质上是一个数组，可以向数组的特定位置写入颜色。
```python
drawPixel(x: int, y: int, color)  # 向(x, y)处写入颜色color
```