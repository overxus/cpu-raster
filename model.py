import json
from vec3 import vec3
from vertex import Vertex3d


class Model:
    def __init__(self, model_json_path: str):
        self.load(model_json_path)
    
    def load(self, model_json_path: str):
        with open(model_json_path, 'r', encoding='utf-8') as fp:
            model_dict = json.load(fp)
        
        self.vertices_dict = {}
        for vertex_dict in model_dict['vertices']:
            index = vertex_dict['index']
            if self.vertices_dict.get(index, None):
                print(f'Warning: index {index} already exists when loading model file {model_json_path}')
            position = vertex_dict['position']
            color = vertex_dict.get('color', [255, 0, 0])
            vertex = Vertex3d(vec3(*position), color)
            self.vertices_dict[index] = vertex
        
        self.triangle_index_buffer = model_dict['triangles']
