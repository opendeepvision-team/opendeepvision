# -*- coding: utf-8 -*-
"""
Abstract components for BaseFaceDetector class.
"""

from abc import abstractmethod

from opendv.utils.template.analytics import BaseDetector

class BaseFaceDetector(BaseDetector):
    """
    Abstract base class for BaseFaceDetector class.
    """

    # Member of FaceDetector1
    @property
    @abstractmethod
    def min_face_size(self):
        raise NotImplementedError
    
    # Member of FaceDetector1
    @property
    @abstractmethod
    def scale_factor(self):
        raise NotImplementedError
    
    # Member of FaceDetector1
    @property
    @abstractmethod
    def steps_threshold(self):
        raise NotImplementedError