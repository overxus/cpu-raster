from vec3 import vec3


class mat3:
    def __init__(self, v1: vec3 = vec3(1.0, 0.0, 0.0)
                     , v2: vec3 = vec3(0.0, 1.0, 0.0)
                     , v3: vec3 = vec3(0.0, 0.0, 1.0)):
        self.data = [
            [v1.x, v1.y, v1.z],
            [v2.x, v2.y, v2.z],
            [v3.x, v3.y, v3.z],
        ]

    def __str__(self) -> str:
        return f'mat3({self.data})'
    
    @staticmethod
    def identity() -> 'mat3':
        return mat3(
            vec3(1.0, 0.0, 0.0),
            vec3(0.0, 1.0, 0.0),
            vec3(0.0, 0.0, 1.0))
    
    @staticmethod
    def zero() -> 'mat3':
        return mat3(
            vec3(0.0, 0.0, 0.0),
            vec3(0.0, 0.0, 0.0),
            vec3(0.0, 0.0, 0.0))
    
    @staticmethod
    def transpose(m: 'mat3') -> 'mat3':
        mt = mat3()
        