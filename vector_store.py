import faiss
import numpy as np


def create_chunks(
    records,
    chunk_size=900,
    overlap=120
):
    """
    Split document text into overlapping chunks.
    """

    chunks = []

    for record in records:

        text = record["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[
                start:end
            ].strip()

            if chunk_text:

                chunks.append(
                    {
                        "text": chunk_text,
                        "source": record["source"],
                        "page": record["page"]
                    }
                )

            if end >= len(text):
                break

            start = end - overlap

    return chunks


def build_faiss_index(
    chunks,
    embedder
):
    """
    Generate embeddings and create
    a FAISS similarity-search index.
    """

    if not chunks:

        return None

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedder.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False
    )

    embeddings = embeddings.astype(
        "float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    return index


def retrieve_documents(
    question,
    index,
    chunks,
    embedder,
    top_k=4
):
    """
    Retrieve the most relevant document chunks
    for the user's question.
    """

    if (
        index is None
        or embedder is None
        or not chunks
    ):

        return []

    query_embedding = embedder.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    query_embedding = query_embedding.astype(
        "float32"
    )

    number_to_retrieve = min(
        top_k,
        len(chunks)
    )

    scores, indices = index.search(
        query_embedding,
        number_to_retrieve
    )

    results = []

    for score, index_number in zip(
        scores[0],
        indices[0]
    ):

        if index_number < 0:
            continue

        chunk = chunks[
            index_number
        ].copy()

        chunk["score"] = float(
            score
        )

        results.append(
            chunk
        )

    return results