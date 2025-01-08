from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding(text: str) -> list:
    """
    Generate an embedding for a given text.
    """
    return embedding_model.embed_query(text)
