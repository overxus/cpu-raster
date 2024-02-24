import math
from vec3 import vec3


def translate(p: vec3, tv: vec3) -> vec3:
    """将点p按向量tv平移"""
    return vec3(p.x + tv.x, p.y + tv.y, p.z + tv.z)


def scale(p: vec3, sv: vec3) -> vec3:
    """将点p按向量tv缩放"""
    return p * sv

def rotate(p: vec3, rv: vec3, theta: float) -> vec3:
    """将点p绕rv顺时针旋转theta，这里的theta是弧度制"""
    proj_rv_p = vec3.projection(p, rv) * vec3.normalize(rv)
    forward = p - proj_rv_p
    right = vec3.cross(rv, forward)

    return forward.length * (
        math.sin(theta) * vec3.normalize(right) + math.cos(theta) * vec3.normalize(forward)
    ) + proj_rv_p
