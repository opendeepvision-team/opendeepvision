# -*- coding: utf-8 -*-
"""
Abstract components for Analytics class.
"""

from abc import ABC,abstractmethod

class BaseAnalytics(ABC):
    """
    Abstract base class for Analytics class.
    """

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def description(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def alias(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def paper_url(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def arxiv_url(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def code_url(self):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def bibtex(self):
        raise NotImplementedError