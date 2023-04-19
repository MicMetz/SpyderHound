from abc import ABC, abstractmethod



class AbstractModel(ABC):
    def __init__(self, dataset):
        self.dataset = dataset



    @property
    @abstractmethod
    def name(self):
        pass


    @property
    @abstractmethod
    def train(self):
        pass
