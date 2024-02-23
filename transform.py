import math
from vec3 import vec3


def translate(p: vec3, tv: vec3) -> vec3:
    """将点p按向量tv平移"""
    return vec3(p.x + tv.x, p.y + tv.y, p.z + tv.z)


def scale(p: vec3, sv: vec3) -> vec3:
    """将点p按向量tv缩放"""
    return p * sv

def rotate(p: vec3, rv: vec3, theta: float) -> vec3:
    """将点p绕rv旋转theta，这里的theta是弧度制"""
    # TODO:
    raise NotImplemented("TODO: 实现旋转变换")
