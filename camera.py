from vec3 import vec3
from vertex import Vertex3d


class Camera:
    WORLDUP = vec3(0, 1, 0)  # 世界坐标系向上的位置

    def __init__(self, position: vec3, lookAt: vec3, distance: float = 1.0, width: float = 1.0, height: float = 1.0):
        """Camera
        Args:
            position: 摄像机的位置
            lookAt: 摄像机的朝向
            distance: 摄像机的顶点据投影平面的位置
            width, height: 投影平面的宽和高
        """
        self.position = position
        self.setLookAt(lookAt)
        self.D = distance
        self.W = width
        self.H = height

    def setLookAt(self, lookAt: vec3):
        self.lookAt = lookAt
        self.right = vec3.cross(Camera.WORLDUP, self.lookAt)
        self.up = vec3.cross(self.lookAt, self.right)

    def view(self, p: vec3) -> vec3:
        """将世界坐标系中的点p变化为摄像机坐标系中的坐标，只需要计算p在每个坐标轴上的投影即可"""
        v_rel = p - self.position  # 相对于摄像机位置的向量
        px = vec3.projection(v_rel, self.right)
        py = vec3.projection(v_rel, self.up)
        pz = vec3.projection(v_rel, self.lookAt)
        return vec3(px, py, pz)
    
    def projection(self, p: vec3) -> vec3:
        """将摄像机坐标系中的点p的x, y标准化到[-1, 1]范围内"""
        px = p.x * self.D / p.z
        py = - p.y * self.D / p.z  # NOTE: 标准化后, 由于左上角坐标为(-1, 1), 因此Y方向上的坐标需要取反
        return vec3(px * 2 / self.W, py * 2 / self.H, p.z)
