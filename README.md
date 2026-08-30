# 📚 Domain-Specific RAG Chatbot for PDF Question Answering

## College Academic Policies & Student Handbook

A domain-specific Retrieval-Augmented Generation (RAG) chatbot designed to answer questions related to college academic policies, regulations, examination guidelines, and student handbook information.

The system retrieves relevant information from university PDF documents and uses Google's Gemini model to generate clear and context-based answers.


## 📌 Project Overview

The **Domain-Specific RAG Chatbot** is an AI-powered document question-answering system developed using Python and Streamlit.

Instead of depending only on the language model's general knowledge, the chatbot first searches the provided university documents for relevant information. The retrieved text is then supplied to the Gemini language model to generate the final answer.

The chatbot is designed specifically for the following application domain:

> **College Academic Policies & Student Handbook**

The system helps students quickly find information about academic regulations, attendance requirements, examination guidelines, academic records, and other university-related policies.


## 🎯 Objectives

- To develop a domain-specific AI chatbot for university documents.
- To retrieve relevant information from PDF documents.
- To generate answers based only on the provided documents.
- To reduce incorrect or unsupported answers.
- To display the actual retrieved source text used by the RAG system.
- To provide document name and page information for retrieved content.
- To create a simple and user-friendly chatbot interface.


## ✨ Features

- 📚 Domain-specific university document question answering
- 📄 PDF document processing
- 🔎 Semantic document retrieval
- 🧠 Sentence Transformer embeddings
- ⚡ FAISS vector similarity search
- 🤖 Google Gemini-powered answer generation
- 📖 Retrieved source text display
- 📌 Source document and page information
- 💬 ChatGPT-style conversational interface
- 🗑 Clear conversation option
- ➕ New chat option
- 💡 Suggested questions
- 📊 Question count tracking
- 🔒 Answers restricted to the provided documents
- 🖥️ Streamlit web interface


## 🏗️ System Architecture

The chatbot follows the Retrieval-Augmented Generation (RAG) architecture:

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Relevant Document Chunks
      ↓
Retrieved Source Text
      ↓
Gemini Language Model
      ↓
Generated Answer
      ↓
Answer + Retrieved Text + Source Information
```


## 🔄 RAG Pipeline

The system works through the following stages:

### 1. Document Loading

The PDF documents stored in the documents/ folder are read using pypdf.

### 2. Text Extraction

Text is extracted from each page of the PDF documents along with:

Document name
Page number
Extracted text

### 3. Text Chunking

The extracted document text is divided into smaller overlapping chunks.

The current implementation uses:

Chunk size: 900 characters
Overlap: 120 characters

### 4. Text Embedding  

The text chunks are converted into numerical vector representations using:

all-MiniLM-L6-v2

from Sentence Transformers.

### 5. FAISS Retrieval

FAISS is used to perform similarity search between the user's question and the stored document embeddings.

The most relevant document chunks are retrieved for each question.

### 6. Gemini Generation

The retrieved document context is provided to Google's Gemini model.

The model is instructed to answer only from the supplied document context and not use outside information.

### 7. Source Display

The chatbot displays the generated answer along with the retrieved source information, including:

Source document
Page number
Actual retrieved text


## 📂 Project Structure

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
├── .gitignore
│
├── documents/
│   ├── Academic_Regulations.pdf
│   ├── Examination_Guidelines.pdf
│   └── Student_Handbook.pdf
│
├── vector_store/
│   ├── index.faiss
│   └── metadata.pkl
│
├── reports/
│   ├── DomaEn-Specific RAG Chatbot_Short Project Report.pdf
│   └── RAG Chatbot_Demonstration Video.mp4
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
    

## 🛠️ Technologies Used

### Technology Used

* **Python** – Main programming language
* **Streamlit** – Web application and chatbot interface
* **FAISS** – Vector database for similarity-based document retrieval
* **Sentence Transformers** – Text embedding generation using `all-MiniLM-L6-v2`
* **Google Gemini API** – AI-powered answer generation
* **PyPDF** – PDF text extraction
* **python-dotenv** – Environment variable and API key management
* **NumPy** – Numerical and embedding data processing
* **Git & GitHub** – Version control and project repository management


## 📚 Documents Used

The chatbot currently uses the following university-related documents:

## 📘 Student Handbook

Contains information related to student policies, academic procedures, and university guidelines.

## 📗 Academic Regulations

Contains academic rules and regulations applicable to students.

## 📕 Examination Guidelines

Contains information related to examinations, academic assessment, and examination procedures.


## 💻 Installation

### 1. Clone the Repository

git clone https://github.com/jothicherina/Domain-Specific_RAG_Chatbot-.git

### 2. Open the Project Folder

cd Domain-Specific_RAG_Chatbot-

### 3. Create a Virtual Environment

python -m venv .venv

### 4. Activate the Virtual Environment

For Windows:

.venv\Scripts\activate

### 5. Install Required Packages

pip install -r requirements.txt


## 🔑 Gemini API Configuration

The chatbot uses the Google Gemini API for answer generation.

Create a .env file in the project root directory:

GEMINI_API_KEY=your_gemini_api_key_here

Replace the placeholder with your actual Gemini API key.

### ⚠️ Important

Do not upload your .env file or Gemini API key to GitHub.

The .env file should remain private.


## ▶️ How to Run

After activating the virtual environment, run:

streamlit run app.py

The application will open in your web browser.


## 💬 How to Use

1. Open the chatbot application.
2. Enter a question related to the university documents.
3. The system converts the question into an embedding.
4. FAISS retrieves the most relevant document chunks.
5. Gemini generates an answer using the retrieved context.
6. The answer is displayed in the chatbot.
7. Open View Retrieved Text to see the actual source text used by the system.
8. The source document and page number are also displayed.


## 💡 Example Questions

What is the minimum attendance requirement?
What are the academic regulations?
What information is provided about academic records?
What happens if a student does not meet the attendance requirement?


## 🔎 Retrieved Text

One of the important features of this project is that the chatbot does not only display the generated answer.

It also provides the actual retrieved text from the relevant university document.

For each retrieved source, the system displays:

Source
Document
Page
Retrieved text from the source

This improves transparency and allows the user to verify where the chatbot obtained the information.


## 🧪 Testing

The project contains multiple test files to verify different components of the RAG system.

```text
tests/
├── test_complete_rag.py
├── test_embeddings.py
├── test_gemini.py
├── test_loader.py
├── test_questions.csv
├── test_rag_pipeline.py
├── test_retrieval.py
└── test_vector_store.py
```

The tests cover areas such as:

- PDF document loading
- Text extraction
- Text embeddings
- Vector store functionality
- Document retrieval
- Gemini integration
- Complete RAG pipeline


## 📊 Expected Output

The chatbot provides:

- User question
- AI-generated answer
- Retrieved source information
- Document name
- Page number
- Actual retrieved text

The system informs the user when the requested information cannot be found in the provided documents.


## 🎥 Project Demonstration

The complete project demonstration video is available in:

reports/RAG_Chatbot_Demonstration.mp4

The project report is available in:

reports/DomaEn-Specific RAG Chatbot_Short Project Report.pdf


## 🔐 Limitations

1. The chatbot can answer only using the information available in the provided documents.
2. The quality of the answer depends on the quality of the extracted PDF text.
3. Scanned PDFs without selectable text may require OCR processing.
4. A valid Gemini API key is required for answer generation.
5. The chatbot is currently focused on the college academic policies and student handbook domain.


## 🚀 Future Enhancements

Possible future improvements include:

- Support for more university documents
- Automatic document uploading through the interface
- OCR support for scanned documents
- Improved retrieval and ranking techniques
- Conversation memory
- Authentication for students and staff
- Deployment as an online application
- More advanced citation and source highlighting
- Multilingual question answering


## 👩‍💻 Project Information

### Project Title:
Domain-Specific RAG Chatbot for PDF Question Answering

### Application Domain:
College Academic Policies & Student Handbook

### Technology:
Python, Streamlit, FAISS, Sentence Transformers, Google Gemini

### Project Type:
Domain-Specific Retrieval-Augmented Generation (RAG) Chatbot

## 📄 License

This project is developed for academic and educational purposes.


## Conclusion

The **Domain-Specific RAG Chatbot** provides an efficient way to access information from college academic policies, regulations, examination guidelines, and the student handbook. By combining **document retrieval, text embeddings, FAISS similarity search, and Google Gemini**, the chatbot generates answers based specifically on the provided university documents. This reduces the need to manually search through lengthy documents and provides quick, relevant, and reliable responses.

Overall, the project demonstrates how **Retrieval-Augmented Generation (RAG)** can be applied to create a practical domain-specific AI assistant for academic information.
