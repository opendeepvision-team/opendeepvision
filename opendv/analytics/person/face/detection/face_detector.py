import os
import json
from skimage.io import imread

from opendv.utils.template import BaseFaceDetector
from opendv.analytics.person.face.detection import FaceDetector1
from opendv.analytics.person.face.detection import FaceDetector2

class FaceDetector(BaseFaceDetector):
    
    def __init__(self, id=None, alias=None, **kwargs):
        algorithm_class_name = self._get_algorithm_class_name(id, alias)
        self._detector = eval(algorithm_class_name)(**kwargs)
    
    def detect(self, file_path):
        image = imread(file_path)
        faces = self._detector.detect(image)
        return faces
    
    def _get_algorithm_class_name(self, id=None, alias=None):
        module_path = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(module_path, 'config.json'), 'r') as f:
            config = json.load(f)
        if id is None and alias is None:
            _id = config['default']
            algorithm_class_name = config['algorithms'][_id]['class_name']
        else:
            algorithms = config["algorithms"]
            if id is None:
                for _,algorithm in algorithms.items():
                    if algorithm["alias"] == alias:
                        algorithm_class_name = algorithm['class_name']
            else:
                _id = str(id)
                algorithm_class_name = algorithms[_id]['class_name']
        return algorithm_class_name
    
    def __str__(self):
        return self._detector.__str__
    
    @property
    def name(self):
        return self._detector.name
    
    @name.setter
    def name(self, value):
        self._detector.name = value
    
    @property
    def description(self):
        return self._detector.description
    
    @description.setter
    def description(self, value):
        self._detector.description = value
    
    @property
    def alias(self):
        return self._detector.alias
    
    @alias.setter
    def alias(self, value):
        self._detector.alias = value
    
    @property
    def paper_url(self):
        return self._detector.paper_url
    
    @paper_url.setter
    def paper_url(self, value):
        self._detector.paper_url = value
    
    @property
    def arxiv_url(self):
        return self._detector.arxiv_url
    
    @arxiv_url.setter
    def arxiv_url(self, value):
        self._detector.arxiv_url = value
    
    @property
    def code_url(self):
        return self._detector.code_url
    
    @code_url.setter
    def code_url(self, value):
        self._detector.code_url = value
    
    @property
    def bibtex(self):
        return self._detector.bibtex
    
    @bibtex.setter
    def bibtex(self, value):
        self._detector.bibtex = value
    
    @property
    def min_face_size(self):
        return self._detector.min_face_size
    
    @min_face_size.setter
    def min_face_size(self, value):
        self._detector.min_face_size = value
    
    @property
    def scale_factor(self):
        return self._detector.scale_factor
    
    @property
    def steps_threshold(self):
        return self._detector.steps_threshold

def main():
    fd = FaceDetector()
    fd.priority = 2
    fd.min_face_size = 30
    print(fd)
    faces = fd.detect('utils/template/faces.jpg')
    print(faces)
    print(len(faces))

def get_config():
    with open('config.json', 'r') as f:
        params = json.load(f)
        print(type(params['priority']))

def test_fd():
    fd = FaceDetector(algorithm='1')
    fd2 = FaceDetector(algorithm='1', scale_factor=0.8, steps_threshold=[1,2], min_face_size=50)
    print(fd.name)
    print(fd.description)
    print(fd.alias)
    print(fd.paper_url)
    print(fd.code_url)
    print(fd.bibtex)
    fd.bibtex = 'naber canim'
    print(fd.bibtex)
    print(fd.min_face_size)
    fd.min_face_size = 40
    print(fd.min_face_size)
    print(fd.scale_factor)
    print(fd.steps_threshold)
    print(fd2.min_face_size)
    fd2.min_face_size = 60
    print(fd2.min_face_size)
    print(fd2.scale_factor)
    print(fd2.steps_threshold)

if __name__ == '__main__':
    #main()
    #create_config()
    #get_config()
    test_fd()