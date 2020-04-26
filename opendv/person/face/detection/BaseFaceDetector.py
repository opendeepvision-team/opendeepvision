# -*- coding: utf-8 *-*
from abc import ABC, abstractmethod

class BaseFaceDetector(ABC):

    @abstractmethod
    def detect(self, path):
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def alias(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def arxiv_url(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def impl_url(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def active(self):
        raise NotImplementedError