from document_loader import (
    extract_text_from_pdf,
    split_documents_into_chunks
)

from vector_store import create_embeddings

from pathlib import Path


documents_folder = Path("Documents")

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


print("\nEmbeddings created successfully!")

print("Number of chunks:", len(chunks))

print("Embedding shape:", embeddings.shape)

print("First embedding:")

print(embeddings[0][:10])