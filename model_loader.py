import json


class Point3d:
    def __init__(self, position: list[int], color: list[int] = [255, 255, 255, 255]):
        assert len(position) == 3
        self.position = tuple(position)

        assert len(color) in (3, 4,)
        if len(color) == 3:
            color.append(255)
        self.color = tuple(color)
    
    @property
    def x(self):
        return self.position[0]
    
    @property
    def y(self):
        return self.position[1]
    
    @property
    def z(self):
        return self.position[2]


class Model:
    def __init__(self, point_index_dict: dict, triangle_index_buffer: list):
        self.point_index_dict = point_index_dict
        self.triangle_index_buffer = triangle_index_buffer
    

def ModelLoader(model_json_path: str) -> Model:
    with open(model_json_path, 'r', encoding='utf-8') as fp:
        model_dict = json.load(fp)
    
    point_index_dict = {}
    for point_dict in model_dict['vertices']:
        index = point_dict['index']
        position = point_dict['position']
        color = point_dict.get('color', [255, 0, 0, 255])
        point3d = Point3d(position, color)
        if point_index_dict.get(index, None):
            print(f'Warning: index {index} has been used in model file {model_json_path}')
        point_index_dict[index] = point3d

    return Model(point_index_dict, model_dict['triangles'])    
