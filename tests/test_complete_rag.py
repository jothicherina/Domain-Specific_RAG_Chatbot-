from rag_pipeline import ask_rag

question = "What is the population of Japan?"

print("Question:")
print(question)
print("\nGenerating answer...")

answer, retrieved_documents = ask_rag(
    question,
    top_k=3
)

print("\n" + "=" * 60)
print("RAG ANSWER")
print("=" * 60)
print(answer)
print("\n" + "=" * 60)
print("RETRIEVED SOURCES")
print("=" * 60)

for number, document in enumerate(
    retrieved_documents,
    start=1
):

    print(f"\nSource {number}")
    print("Document:", document["source"])
    print("Page:", document["page"])
    print("Distance:", document["distance"])