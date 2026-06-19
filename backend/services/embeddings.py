from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

class EmbeddingModel:

    def embed_query(self, text):
        return model.encode(text).tolist()

embedding_model = EmbeddingModel()