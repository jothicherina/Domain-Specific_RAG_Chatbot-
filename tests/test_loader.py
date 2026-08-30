from document_loader import (
    extract_text_from_pdf,
    split_documents_into_chunks
)

from pathlib import Path

documents_folder = Path("Documents")

pdf_files = list(documents_folder.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files.\n")


all_documents = []

for pdf_file in pdf_files:

    print("=" * 60)
    print(f"Reading: {pdf_file.name}")
    print("=" * 60)

    documents = extract_text_from_pdf(pdf_file)

    print(f"Pages extracted: {len(documents)}")

    all_documents.extend(documents)


print("\n" + "=" * 60)
print("CREATING CHUNKS")
print("=" * 60)


chunks = split_documents_into_chunks(all_documents)


print(f"\nTotal chunks created: {len(chunks)}")


print("\nFirst 5 chunks:\n")


for number, chunk in enumerate(chunks[:5], start=1):

    print("-" * 60)
    print(f"Chunk {number}")
    print(f"Source: {chunk['metadata']['source']}")
    print(f"Page: {chunk['metadata']['page']}")
    print(f"Characters: {len(chunk['text'])}")
    print(f"Text: {chunk['text'][:300]}...")