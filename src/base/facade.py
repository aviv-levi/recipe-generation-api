from src.core.stage import IStage


class Facade:
    def __init__(self, stage: IStage):
        self._stage = stage

    def start(self):
        query = "pasta recipe"
        response = self._stage.run(query)
        print(response)
