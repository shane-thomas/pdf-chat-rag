# Chat with PDFs 📚

This project allows users to interact with PDF documents by uploading them, and then asking questions about the content. Using gemma3, the app extracts relevant information from the uploaded PDF and provides concise, accurate answers. It's a simple but powerful way to extract knowledge from documents and communicate with them efficiently.

## Features

- **PDF Upload**: Upload PDF files to the app for processing.
- **Document Processing**: The app splits PDF text into chunks and stores them in a vector database.
- **Ask Questions**: Once the document is processed, you can ask questions related to the PDF content.
- **Chat Interface**: Provides a simple chat interface where users can interact with the PDF-based assistant.

## Prerequisites

Before running this app, make sure you have the following installed:

- **Ollama**: This app relies on Ollama for embeddings and language model support. You need to install the Ollama library and have a supported model (e.g., "gemma3") set up. [Ollama Installation](https://ollama.com/)
- **Python Libraries**: Make sure you have the required Python libraries installed. You can do this by running:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes all necessary dependencies, such as `streamlit`, `langchain`, `faiss`, and `PyPDF2`.

## How to Run the App

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/shane-thomas/pdf-chat-rag.git
    cd pdf-chat-rag
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the App**:

    ```bash
    streamlit run app.py
    ```

4. Open the provided URL in your browser to interact with the app.
   
### 🖼 Example Screenshot

<img src="https://github.com/shane-thomas/pdf-chat-rag/blob/main/screenshot?raw=true" alt="Example Screenshot" width="800"/>

## How It Works

1. **Upload PDF**: The user uploads a PDF document using the file uploader in the app.
2. **Processing**: The PDF is processed, and its content is split into chunks for better search and retrieval. These chunks are stored in a vector database.
3. **Ask Questions**: After processing, you can ask questions about the PDF. The app will retrieve the most relevant information from the vector store and provide concise answers based on the content.
4. **Answering**: The assistant uses the context from the document to generate a precise answer to your question.
