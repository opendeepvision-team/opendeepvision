# -*- coding: utf-8 -*-
"""
Abstract components for BaseDetector class.
"""

from abc import abstractmethod

from base_analytics import BaseAnalytics

class BaseDetector(BaseAnalytics):
    """
    Abstract base class for BaseDetector class.
    """

    @abstractmethod
    def detect(self, *args, **kwargs):
        raise NotImplementedError