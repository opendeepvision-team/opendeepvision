import os
import json
from mtcnn import MTCNN
from skimage.io import imread

from opendv.utils.template.analytics import BaseFaceDetector

class FaceDetector1(BaseFaceDetector):

    def __init__(self, **kwargs):
        algorithm = self._get_algorithm()
        params = {}
        for k,v in kwargs.items():
            params[k] = v
        self._name = algorithm['name']
        self._description = algorithm['description']
        self._alias = algorithm['alias']
        self._paper_url = algorithm['paper_url']
        self._arxiv_url = algorithm['arxiv_url']
        self._code_url = algorithm['code_url']
        self._bibtex = algorithm['bibtex']
        self._class_name = algorithm['class_name']
        self._min_face_size = params.get('min_face_size', 20)
        self._scale_factor = params.get('scale_factor', 0.709)
        self._steps_threshold = params.get('steps_threshold', None)
        self._detector = MTCNN(min_face_size=self._min_face_size, 
                               scale_factor=self._scale_factor, 
                               steps_threshold=self._steps_threshold)
    
    def detect(self, image):
        faces = self._detector.detect_faces(image)
        return faces

    def _get_algorithm(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(module_path, 'config.json'), 'r') as f:
            config = json.load(f)
            algorithms = config["algorithms"]
            for id,algorithm in algorithms.items():
                if algorithm["class_name"] == self.__class__.__name__:
                    return algorithm
    
    def __str__(self):
        return '\n'.join([
            str(self._min_face_size), 
            str(self._scale_factor), 
            str(self._steps_threshold), 
            self._name, 
            self._description, 
            self._alias, 
            self._paper_url, 
            self._arxiv_url, 
            self._code_url, 
            self._bibtex])
    
    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description
    
    @property
    def alias(self):
        return self._alias
    
    @property
    def paper_url(self):
        return self._paper_url
    
    @property
    def arxiv_url(self):
        return self._arxiv_url
    
    @property
    def code_url(self):
        return self._code_url
    
    @property
    def bibtex(self):
        return self._bibtex
    
    @property
    def class_name(self):
        return self._class_name
    
    @property
    def min_face_size(self):
        return self._min_face_size
    
    @min_face_size.setter
    def min_face_size(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._min_face_size = value
        self._detector.min_face_size = value
    
    @property
    def scale_factor(self):
        return self._scale_factor
    
    @property
    def steps_threshold(self):
        return self._steps_threshold

def main():
    fd = FaceDetector1()
    fd.priority = 2
    fd.min_face_size = 30
    print(fd)
    faces = fd.detect('utils/template/faces.jpg')
    print(faces)
    print(len(faces))

if __name__ == '__main__':
    main()