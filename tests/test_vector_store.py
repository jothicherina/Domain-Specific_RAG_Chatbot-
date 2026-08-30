from document_loader import (
    extract_text_from_pdf,
    split_documents_into_chunks
)

from vector_store import (
    create_embeddings,
    create_faiss_index,
    save_vector_store
)

from pathlib import Path


documents_folder = Path("documents")

pdf_files = list(documents_folder.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files.\n")


all_documents = []


for pdf_file in pdf_files:

    print(f"Reading: {pdf_file.name}")

    documents = extract_text_from_pdf(pdf_file)

    all_documents.extend(documents)


print("\nCreating chunks...")

chunks = split_documents_into_chunks(all_documents)

print(f"Total chunks: {len(chunks)}")


print("\nCreating embeddings...")

embeddings = create_embeddings(chunks)

print("Embeddings created!")


print("\nCreating FAISS index...")

index, metadata = create_faiss_index(
    chunks,
    embeddings
)


print("FAISS index created!")

print("Number of vectors:", index.ntotal)

print("Embedding dimension:", index.d)


print("\nSaving vector store...")

save_vector_store(
    index,
    metadata
)