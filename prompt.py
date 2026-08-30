def build_prompt(
    question,
    retrieved_chunks
):
    """
    Create the prompt sent to Gemini using
    only the retrieved document context.
    """

    context_parts = []

    for i, chunk in enumerate(
        retrieved_chunks,
        start=1
    ):

        context_parts.append(
            f"""
SOURCE {i}

Document: {chunk['source']}

Page: {chunk['page']}

Content:

{chunk['text']}
"""
        )

    context = "\n".join(
        context_parts
    )

    prompt = f"""
You are a domain-specific university document assistant.

Answer the user's question ONLY using the supplied
document context.

IMPORTANT RULES:

1. Do not invent information.
2. Do not use outside knowledge.
3. Do not make assumptions.
4. If the answer is not available in the supplied
   documents, say:

"I could not find this information in the uploaded documents."

5. Give a clear and useful answer.
6. Use normal Markdown if formatting is helpful.
7. Do not output HTML.
8. Do not output HTML tags.
9. Do not output CSS.
10. Mention the document name and page number when useful.

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""

    return prompt