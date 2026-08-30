from rag_pipeline import retrieve_documents

question = "What is the minimum attendance requirement?"
results = retrieve_documents(question, top_k=3)

print("Question:")
print(question)

print("\nRetrieved documents:")

for number, result in enumerate(results, start=1):

    print("\n" + "=" * 60)
    print(f"Result {number}")
    print("Source:", result["source"])
    print("Page:", result["page"])
    print("Distance:", result["distance"])
    print("\nText:")
    print(result["text"])