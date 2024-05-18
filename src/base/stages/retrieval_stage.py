from src.base.base_stage import BaseStage

__all__ = ['RetrievalStage']


class RetrievalStage(BaseStage):

    def run(self, data):
        print('RetrievalStage')
        super().run(data)
