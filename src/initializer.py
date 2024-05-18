import os
import datasets
from src.base.facade import Facade
import faiss
from transformers import DPRContextEncoderTokenizer, DPRContextEncoder, BartTokenizer, BartForConditionalGeneration
from src.base.stages import RetrievalStage, GenerativeStage


class Initializer:

    def initialize_vector_db(self):
        vector_db_path = os.getenv("VECTOR_DB_PATH", "notebooks/recipes_index.idx")
        vector_db = faiss.read_index(vector_db_path)
        return vector_db

    def initialize_recipes(self):
        dataset_path = os.getenv("DATASET_PATH", "notebooks/dataset")
        dataset = datasets.load_from_disk(dataset_path)
        recipes = [entry['steps'] for entry in dataset['train']]
        return recipes

    def initialize(self) -> Facade:
        recipes = self.initialize_recipes()
        vector_db = self.initialize_vector_db()
        tokenizer = DPRContextEncoderTokenizer.from_pretrained('facebook/dpr-ctx_encoder-multiset-base')
        model = DPRContextEncoder.from_pretrained('facebook/dpr-ctx_encoder-multiset-base')
        bart_tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
        bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

        retrieval_stage = RetrievalStage(tokenizer=tokenizer, model=model, vector_db=vector_db, recipes=recipes)
        generative_stage = GenerativeStage(bart_tokenizer=bart_tokenizer, bart_model=bart_model)

        return Facade(retrieval_stage=retrieval_stage, generative_stage=generative_stage)

