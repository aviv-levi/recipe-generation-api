from src.base.base_stage import BaseStage

__all__ = ['GenerativeStage']


class GenerativeStage(BaseStage):

    def run(self, data):
        print('GenerativeStage')
        super().run(data)
