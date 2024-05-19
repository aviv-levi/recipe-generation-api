from src.base.stages.base_stage import BaseStage

__all__ = ['RetrievalStage']


class RetrievalStage(BaseStage):

    def __init__(self, tokenizer, model, vector_db, recipes):
        super().__init__()
        self._k = 5
        self._tokenizer = tokenizer
        self._model = model
        self._vector_db = vector_db
        self._recipes = recipes

    def _encode_query(self, query):
        inputs = self._tokenizer([query], return_tensors='pt', padding=True, truncation=True, max_length=512)
        embeddings = self._model(**inputs).pooler_output
        return embeddings.detach().numpy()

    def run(self, query):
        # encode desire recipe and search for top-k recipes from vector-db
        query_embedding = self._encode_query(query=query)
        vectors_distances, vectors_indices = self._vector_db.search(query_embedding, self._k)
        # retrieve original top-k recipes
        relevant_recipes = [self._recipes[i] for i in vectors_indices[0]]
        return super().run((relevant_recipes, query))
