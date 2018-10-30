# __*__ coding: utf-8 __*__
from abc import abstractmethod, ABCMeta


class Processor:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def process(self, file_path):
        pass
