import os
import json
from retinaface import RetinaFace
from skimage.io import imread

from opendv.utils.template.analytics import BaseFaceDetector

class FaceDetector2(BaseFaceDetector):

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
    
    def detect(self, image):
        faces = RetinaFace.detect_faces(image)
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
        raise NotImplementedError
    
    @min_face_size.setter
    def min_face_size(self, value):
        raise NotImplementedError
    
    @property
    def scale_factor(self):
        raise NotImplementedError
    
    @property
    def steps_threshold(self):
        raise NotImplementedError