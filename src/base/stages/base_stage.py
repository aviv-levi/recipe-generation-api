from src.core.stage import IStage


class BaseStage(IStage):

    def __init__(self):
        self._next_stage: IStage = None

    def connect_next(self, next_stage: IStage):
        self._next_stage = next_stage
        return self._next_stage

    def run(self, data):
        if self._next_stage:
            return self._next_stage.run(data)
        return data

