from src.base.stages.base_stage import BaseStage

__all__ = ['GenerativeStage']


class GenerativeStage(BaseStage):

    def __init__(self, bart_tokenizer, bart_model):
        super().__init__()
        self._bart_tokenizer = bart_tokenizer
        self._bart_model = bart_model

    def run(self, data):
        relevant_recipes, query = data
        combined_relevant_recipes = " ".join(relevant_recipes) + " " + query
        encoded_relevant_recipes = self._bart_tokenizer(combined_relevant_recipes,
                                                        return_tensors='pt', max_length=1024, truncation=True)
        generated_encoded_recipe = self._bart_model.generate(encoded_relevant_recipes['input_ids'],
                                                             max_length=150, num_beams=5, early_stopping=True)
        generated_recipe = self._bart_tokenizer.decode(generated_encoded_recipe[0], skip_special_tokens=True)
        return super().run(generated_recipe)
