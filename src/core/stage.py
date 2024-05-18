from abc import ABC, abstractmethod


class IStage(ABC):

    @abstractmethod
    def connect_next(self, next_stage):
        pass

    @abstractmethod
    def run(self, data):
        pass
