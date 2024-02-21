import math 


class vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x, self.y, self.z = x, y, z
    
    def __add__(self, other: 'vec3') -> 'vec3':
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'vec3') -> 'vec3':
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other) -> 'vec3':
        if isinstance(other, vec3):
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, float) or isinstance(other, int):
            return vec3(self.x * other, self.y * other, self.z * other)
    
    def __rmul__(self, other) -> 'vec3':
        return self.__mul__(other)
    
    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __str__(self) -> str:
        return f'vec3({self.x}, {self.y}, {self.z})'

    @staticmethod
    def normalize(v: 'vec3') -> 'vec3':
        len_v = v.length
        if len_v == 0:
            return v
        else:
            return vec3(v.x / len_v, v.y / len_v, v.z / len_v)
    
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

    print(i.length, (i + j).length)

    print(vec3.projection(i + j, i))
    print(vec3.projection(i + j, j))

    print(vec3.normalize(i + j))

    print(vec3.cross(i, j), vec3.cross(j, i), vec3.cross(i, k), vec3.cross(k, i))
