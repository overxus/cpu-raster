from vec3 import vec3


class Camera:
    def __init__(self, position: vec3, lookAt: vec3, up: vec3,
                 distance: float = 1.0, view_width: float = 1.0, view_height: float = 1.0):
        self.position = position
        self.lookAt = lookAt
        self.up = up
        self.right = vec3.cross(self.up, self.lookAt)
        
        self.__D = distance
        self.__W = view_width
        self.__H = view_height


    def point2canvas(self, p: vec3) -> tuple[float, float]:
        """return (x, y), x, y in [-1, 1]"""
        v_rel = p - self.position
        pz = vec3.projection(v_rel, self.lookAt)
        py = vec3.projection(v_rel, self.up)
        px = vec3.projection(v_rel, self.right)

        return (self.__D * px / pz) / (self.__W / 2), (self.__D * py / pz) / (self.__H / 2)
