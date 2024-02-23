from vec3 import vec3


class Camera:
    def __init__(self, position: vec3, lookAt: vec3, worldup: vec3,
                 distance: float = 1.0, view_width: float = 1.0, view_height: float = 1.0):
        self.position = position
        self.lookAt = lookAt
        self.worldup = worldup
        self.right = vec3.cross(self.worldup, self.lookAt)
        self.up = vec3.cross(self.lookAt, self.right)

        self.__D = distance
        self.__W = view_width
        self.__H = view_height


    def view(self, p: vec3) -> vec3:
        """return (x, y, z), x, y in [-1, 1]"""
        v_rel = p - self.position
        pz = vec3.projection(v_rel, self.lookAt)
        py = vec3.projection(v_rel, self.up)
        px = vec3.projection(v_rel, self.right)

        return vec3((self.__D * px / pz) / (self.__W / 2), - (self.__D * py / pz) / (self.__H / 2), pz)
