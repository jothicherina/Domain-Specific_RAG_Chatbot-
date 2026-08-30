# Domain-Specific RAG Chatbot for PDF Question Answering

## Project Description

The Domain RAG Chatbot is a Retrieval-Augmented Generation (RAG) based chatbot that answers user questions using information retrieved from a set of domain-specific PDF documents.

The system combines document processing, text embeddings, FAISS vector search, and a generative AI model to provide document-grounded answers.


## Features

- Upload and process domain-specific PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate vector embeddings
- Store embeddings using FAISS
- Retrieve relevant document chunks
- Generate answers using Gemini
- Display retrieved sources and page numbers
- Support conversational follow-up questions
- Refuse to answer when information is not available in the provided documents
- Streamlit-based user interface


## Technologies Used

- Python
- Streamlit
- PyPDF
- Sentence Transformers
- FAISS
- Google Gemini API
- python-dotenv


## Project Structure

```text
domain_rag_chatbot/
│
├── app.py
├── rag_pipeline.py
├── document_loader.py
├── vector_store.py
├── prompt.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── documents/
│   ├── Academic_Regulations.pdf
│   ├── Examination_Guidelines.pdf
│   └── Student_Handbook.pdf
│
├── vector_store/
│   ├──index.faiss
│   ├──metadata.pkl
│
└── tests/
    ├── test_complete_rag.py
    ├── test_embeddings.py
    ├── test_gemini.py
    ├── test_loader.py
    ├── test_questions.csv
    ├── test_rag_pipeline.py
    ├── test_retrieval.py
    └── test_vector_store.py
```


## RAG Pipeline
PDF Documents
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Store
      ↓
User Question
      ↓
Similarity Retrieval
      ↓
Relevant Document Chunks
      ↓
Gemini
      ↓
Grounded Answer


## Testing

The chatbot is tested using both in-domain and out-of-domain questions.

The testing process verifies:

- Correct answers from the provided documents
- Retrieval of relevant document information
- Conversation follow-up handling
- Source and page display
- Refusal of unsupported questions


## Installation

Create and activate a Python virtual environment and install the required dependencies:

pip install -r requirements.txt


## Environment Variables

Create a .env file and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

Do not share or upload the .env file publicly.


## Running the Application

Run:

streamlit run app.py

The application will open in the browser.


## Usage
1. Open the chatbot.
2. Enter a question related to the provided documents.
3. Submit the question.
4. Read the generated answer.
5. Open "View Sources" to inspect the retrieved document information.
6. Ask follow-up questions if required.


## Expected Behavior

The chatbot should answer questions using information available in the provided documents.

If the requested information cannot be found in the documents, the chatbot should indicate that the information is unavailable rather than generating an unsupported answer