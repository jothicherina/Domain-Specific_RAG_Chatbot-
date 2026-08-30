import os

import streamlit as st

from sentence_transformers import SentenceTransformer
from google import genai

from dotenv import load_dotenv

from document_loader import (
    load_documents,
    get_full_page_text
)

from vector_store import (
    create_chunks,
    build_faiss_index,
    retrieve_documents
)

from prompt import build_prompt


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

if GEMINI_API_KEY:

    client = genai.Client(
        api_key=GEMINI_API_KEY
    )

else:

    client = None


# ============================================================
# EMBEDDING MODEL
# ============================================================

@st.cache_resource(
    show_spinner=False
)
def load_embedding_model():

    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


# ============================================================
# BUILD RAG SYSTEM
# ============================================================

@st.cache_resource(
    show_spinner=False
)
def build_rag_system():

    # --------------------------------------------------------
    # LOAD PDF DOCUMENTS
    # --------------------------------------------------------

    records = load_documents()

    # --------------------------------------------------------
    # CREATE CHUNKS
    # --------------------------------------------------------

    chunks = create_chunks(
        records
    )

    if not chunks:

        return (
            None,
            [],
            None
        )

    # --------------------------------------------------------
    # LOAD EMBEDDING MODEL
    # --------------------------------------------------------

    embedder = (
        load_embedding_model()
    )

    # --------------------------------------------------------
    # CREATE FAISS INDEX
    # --------------------------------------------------------

    index = build_faiss_index(
        chunks,
        embedder
    )

    return (
        index,
        chunks,
        embedder
    )


# ============================================================
# RETRIEVE DOCUMENTS
# ============================================================

def retrieve(
    question,
    index,
    chunks,
    embedder,
    top_k=4
):

    results = retrieve_documents(
        question,
        index,
        chunks,
        embedder,
        top_k
    )

    # --------------------------------------------------------
    # ADD FULL ORIGINAL PAGE TEXT
    # --------------------------------------------------------

    for result in results:

        full_page_text = (
            get_full_page_text(
                result["source"],
                result["page"]
            )
        )

        if full_page_text:

            result[
                "retrieved_text"
            ] = full_page_text

        else:

            result[
                "retrieved_text"
            ] = result["text"]

    return results


# ============================================================
# GENERATE ANSWER
# ============================================================

def generate_answer(
    question,
    retrieved_chunks
):

    if not retrieved_chunks:

        return (
            "I could not find this information "
            "in the uploaded documents."
        )


    # --------------------------------------------------------
    # CREATE PROMPT
    # --------------------------------------------------------

    prompt = build_prompt(
        question,
        retrieved_chunks
    )


    # --------------------------------------------------------
    # CHECK API KEY
    # --------------------------------------------------------

    if client is None:

        return (
            "Gemini API key is not configured. "
            "Please add GEMINI_API_KEY to your .env file."
        )


    # --------------------------------------------------------
    # GEMINI GENERATION
    # --------------------------------------------------------

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        answer = response.text

        if not answer:

            answer = (
                "I could not find this information "
                "in the uploaded documents."
            )

        return answer.strip()


    except Exception as e:

        print(
            f"Gemini error: {e}"
        )

        return (
            "Unable to generate an answer right now. "
            "Please check your Gemini API configuration."
        )


# ============================================================
# COMPLETE RAG FUNCTION
# ============================================================

def ask_rag(
    question,
    index,
    chunks,
    embedder,
    top_k=4
):

    retrieved_chunks = retrieve(
        question,
        index,
        chunks,
        embedder,
        top_k
    )

    answer = generate_answer(
        question,
        retrieved_chunks
    )

    return (
        answer,
        retrieved_chunks
    )