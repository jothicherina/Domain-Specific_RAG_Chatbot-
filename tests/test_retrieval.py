from sentence_transformers import SentenceTransformer

from vector_store import load_vector_store


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# Load the saved FAISS vector store
index, metadata = load_vector_store()

print("FAISS vector store loaded successfully!")
print("Number of vectors:", index.ntotal)


# Load the embedding model
model = SentenceTransformer(MODEL_NAME)


# Question asked by the user
question = "What is the minimum attendance requirement?"


# Convert the question into an embedding
question_embedding = model.encode(
    [question]
).astype("float32")


# Search for the 3 most relevant chunks
distances, indices = index.search(
    question_embedding,
    3
)


print("\nQuestion:")
print(question)


print("\nMost relevant results:")


for rank, index_number in enumerate(indices[0], start=1):

    result = metadata[index_number]

    print("\n" + "=" * 60)
    print(f"Result {rank}")

    print("Source:", result["source"])
    print("Page:", result["page"])

    print("\nText:")
    print(result["text"])

    print("\nDistance:", distances[0][rank - 1])