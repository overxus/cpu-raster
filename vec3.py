import math 
from typing import Union, Iterator


class vec3:
    DELTA = 1e-5  # 判断浮点数精度的误差

    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z

    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self) -> str:
        return f'vec3({self.x:.2f}, {self.y:.2f}, {self.z:.2f})'
    
    def __iter__(self) -> Iterator[float]:
        return (self.x, self.y, self.z)
    
    def __add__(self, other) -> 'vec3':
        if isinstance(other, vec3):
            return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return vec3(self.x + other, self.y + other, self.z + other)
        else:
            raise ValueError('vec3 should add with vec3, float or int, not type', type(other))
    
    def __radd__(self, other) -> 'vec3':
        return self.__add__(other)

    def __neg__(self) -> 'vec3':
        return vec3(-self.x, -self.y, -self.z)
    
    def __sub__(self, other) -> 'vec3':
        try:
            return self.__add__(-other)
        except:
            raise ValueError('vec3 should subtract with vec3, float or int, not type', type(other))
    
    def __rsub__(self, other) -> 'vec3':
        try:
            return self.__neg__().__add__(other)
        except:
            raise ValueError('vec3 should subtract with vec3, float or int, not type', type(other))

    def __mul__(self, other) -> 'vec3':
        if isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return vec3(self.x * other, self.y * other, self.z * other)
        else:
            raise ValueError('vec3 should mulitiply with vec3, float or int, not type', type(other))
    
    def __rmul__(self, other) -> 'vec3':
        return self.__mul__(other)
    
    def __eq__(self, other: 'vec3') -> bool:
        if isinstance(other, vec3):
            return (self - other).length < vec3.DELTA
        else:
            raise ValueError('vec3 should equal with vec3, not type', type(vec3))

    @staticmethod
    def normalize(v: 'vec3') -> 'vec3':
        len_v = v.length
        return vec3(v.x / len_v, v.y / len_v, v.z / len_v) if len_v > 0 else v
        
    @staticmethod
    def dot(u: 'vec3', v: 'vec3') -> float:
        return u.x * v.x + u.y * v.y + u.z * v.z
    
    @staticmethod
    def cross(u: 'vec3', v: 'vec3') -> 'vec3':
        return vec3(u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x)

    @staticmethod
    def projection(u: 'vec3', v: 'vec3') -> float:
        """projection u onto v, return projection length"""
        v_len = v.length
        if v_len == 0:
            raise ValueError('projection vector v should be a non-zero vector')
        else:
            return vec3.dot(u, v) / v_len
        

if __name__ == '__main__':
    i = vec3(1, 0, 0)
    j = vec3(0, 1, 0)
    k = vec3(0, 0, 1)

    # 测试基本运算
    assert i + j == vec3(1, 1, 0)
    assert i + 1 == vec3(2, 1, 1)
    assert i + 2.3 == vec3(3.3, 2.3, 2.3)
    assert 2.3 + i == i + 2.3
    
    assert i - j == vec3(1, -1, 0)
    assert j - i == vec3(-1, 1, 0)
    assert i - 0.3 == vec3(0.7, -0.3, -0.3)
    assert 0.3 - i == vec3(-0.7, 0.3, 0.3)
    assert -1.7 - i == -(i + 1.7)
    assert 2.3 - j == -(j - 2.3)

    assert 0.4 * i == vec3(0.4, 0, 0)
    assert 0.4 * i == i * 0.4

    assert i.length == 1
    assert (i + j).length == math.sqrt(2)
    assert (i - j - k).length == math.sqrt(3)

    # 测试静态方法
    assert vec3.dot(i, j) == 0
    assert vec3.dot(i+j, j) == 1
    assert vec3.dot(i+j+k, j+k) == 2
    
    assert vec3.cross(i, j) == k
    assert vec3.cross(j, k) == i
    assert vec3.cross(k, i) == j

    assert vec3.projection(i + j, i) == 1
    assert vec3.projection(i + j, 2 * i) == 1
