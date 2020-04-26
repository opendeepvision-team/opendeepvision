# -*- coding: utf-8 *-*
from .BaseFaceDetector import BaseFaceDetector

from mtcnn import MTCNN
from cv2 import cv2

class MtcnnFaceDetector(BaseFaceDetector):

    MIN_FACE_SIZE = 20
    SCALE_FACTOR = 0.709

    def __init__(self, weights_file=None, min_face_size=MIN_FACE_SIZE, scale_factor=SCALE_FACTOR):
        self._face_detector = MTCNN(weights_file=weights_file, \
                                    min_face_size=min_face_size, \
                                    scale_factor=scale_factor)
        self._min_face_size = min_face_size
        self._scale_factor = scale_factor
        self._name = 'Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks'
        self._alias = 'mtcnn'
        self._arxiv_url = 'https://arxiv.org/abs/1604.02878'
        self._impl_url = 'https://github.com/ipazc/mtcnn'
        self._active = True

    def detect(self, path):
        if self._min_face_size != self.MIN_FACE_SIZE:
            self._face_detector.min_face_size = self._min_face_size
        img = cv2.imread(path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_dets = self._face_detector.detect_faces(img_rgb)
        return face_dets
    
    @property
    def min_face_size(self):
        return self._min_face_size
    
    @property
    def scale_factor(self):
        return self._scale_factor
    
    @property
    def name(self):
        return self._name

    @property
    def alias(self):
        return self._alias

    @property
    def arxiv_url(self):
        return self._arxiv_url

    @property
    def impl_url(self):
        return self._impl_url

    @property
    def active(self):
        return self._active

    @min_face_size.setter
    def min_face_size(self, value):
        self._min_face_size = value

    @active.setter
    def active(self, value):
        self._active = value
    
    def __str__(self):
        return '\n'.join(['-' * 50, \
                            'Method Name: {}'.format(self._name), \
                            'Alias Name: {}'.format(self._alias), \
                            'Arxiv URL: {}'.format(self._arxiv_url), \
                            'Implementation URL: {}'.format(self._impl_url), \
                            '-' * 50])