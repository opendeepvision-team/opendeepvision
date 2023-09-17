import json
from mtcnn import MTCNN
from skimage.io import imread

from utils.template import BaseFaceDetector

class FaceDetector1(BaseFaceDetector):

    def __init__(self, **kwargs):
        config = self._get_config()
        print(config)
        params = {}
        for k,v in kwargs.items():
            params[k] = v
        self._name = config['name']
        self._description = config['description']
        self._alias = config['alias']
        self._paper_url = config['paper_url']
        self._arxiv_url = config['arxiv_url']
        self._code_url = config['code_url']
        self._bibtex = config['bibtex']
        self._min_face_size = params.get('min_face_size', 20)
        self._scale_factor = params.get('scale_factor', 0.709)
        self._steps_threshold = params.get('steps_threshold', None)
        self._detector = MTCNN(min_face_size=self._min_face_size, 
                               scale_factor=self._steps_threshold, 
                               steps_threshold=self._steps_threshold)
    
    def detect(self, image):
        faces = self._detector.detect_faces(image)
        return faces

    def _get_config(self):
        with open('utils/template/config.json', 'r') as f:
            config = json.load(f)
            algorithms = config["algorithms"]
            for id,algorithm in algorithms.items():
                if algorithm["class_name"] == 'FaceDetector1':
                    return algorithm
    
    def __str__(self):
        return '\n'.join([
            str(self._min_face_size), 
            str(self._scale_factor), 
            str(self._steps_threshold), 
            str(self._priority), 
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
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._name = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._description = value
    
    @property
    def alias(self):
        return self._alias
    
    @alias.setter
    def alias(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._alias = value
    
    @property
    def paper_url(self):
        return self._paper_url
    
    @paper_url.setter
    def paper_url(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._paper_url = value
    
    @property
    def arxiv_url(self):
        return self._arxiv_url
    
    @arxiv_url.setter
    def arxiv_url(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._arxiv_url = value
    
    @property
    def code_url(self):
        return self._code_url
    
    @code_url.setter
    def code_url(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._code_url = value
    
    @property
    def bibtex(self):
        print('aha bi daha girdi')
        return self._bibtex
    
    @bibtex.setter
    def bibtex(self, value):
        if not isinstance(value, str):
            raise TypeError
        print('girdi girdi')
        self._bibtex = value
    
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

def create_config():
    config = {
        "default": "1",
        "algorithms": {
            "1": {
                "name": "MTCNN", 
                "description": "Joint face detection and alignment using multitask cascaded convolutional networks",
                "alias": "mtcnn",
                "paper_url": "https://arxiv.org/abs/1604.02878",
                "code_url": "https://github.com/ipazc/mtcnn",
                "bibtex": "https://arxiv.org/abs/1604.02878", 
                "class_name": "FaceDetector1"
            }
        }
    }
    with open('config.json', 'w') as f:
        json.dump(config, f)

def get_config():
    with open('utils/template/config.json', 'r') as f:
        params = json.load(f)
        print(type(params['default']))
        print(type(params['algorithms']["1"]["class_name"]))
        id = params['default']
        algorithm = params["algorithms"][id]
        fd = eval(algorithm["class_name"])(min_face_size=40)
        #fd = globals()[algorithm["class_name"]](min_face_size=40)
        print(fd.min_face_size)
        fd2 = FaceDetector1()
        print(fd2.min_face_size)

if __name__ == '__main__':
    #main()
    #create_config()
    get_config()