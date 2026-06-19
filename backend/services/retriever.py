from services.embeddings import (
    embedding_model
)

from vectorstore.chroma_store import (
    collection
)


def retrieve_chunks(
    question: str,
    file_id: str,
    user_id: str,
    k: int = 5
):
       #creating an embedding of the question
    query_embedding = (
        embedding_model.embed_query(
            question
        )
    )
 #chromadb search
    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=k
    )

    retrieved_chunks = []
    retrieved_metadata = []

    docs = results.get(
        "documents",
        []
    )

    metas = results.get(
        "metadatas",
        []
    )

    if docs:

        for idx, doc in enumerate(
            docs[0]
        ):

            metadata = metas[0][idx]

            if (
                metadata["file_id"]
                == file_id
                and
                metadata["user_id"]
                == user_id
            ):

                retrieved_chunks.append(
                    doc
                )

                retrieved_metadata.append(
                    metadata
                )

    return {
        "chunks": retrieved_chunks,
        "metadata": retrieved_metadata
    }
    
def retrieve_chunks_across_documents(
    question: str,
    user_id: str,
    k: int = 10
):

    query_embedding = (
        embedding_model.embed_query(
            question
        )
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=k
    )

    retrieved_chunks = []
    retrieved_metadata = []

    docs = results.get(
        "documents",
        []
    )

    metas = results.get(
        "metadatas",
        []
    )

    if docs:

        for idx, doc in enumerate(
            docs[0]
        ):

            metadata = metas[0][idx]

            if (
                metadata["user_id"]
                == user_id
            ):

                retrieved_chunks.append(
                    doc
                )

                retrieved_metadata.append(
                    metadata
                )

    return {
        "chunks":
        retrieved_chunks,

        "metadata":
        retrieved_metadata
    }