# -*- coding: utf-8 -*-
"""
Abstract components for BaseDetector class.
"""

from abc import abstractmethod

from opendv.utils.template import BaseAnalytics

class BaseDetector(BaseAnalytics):
    """
    Abstract base class for BaseDetector class.
    """

    @abstractmethod
    def detect(self, *args, **kwargs):
        raise NotImplementedError