# mini-rag-app

A lightweight Retrieval-Augmented Generation (RAG) application for searching and querying local documents using a small AI workflow.

## Overview

This project demonstrates a minimal RAG setup that:

- loads and indexes local documents
- chunks text for retrieval
- stores embeddings for semantic search
- retrieves relevant context
- combines the retrieved context with a language model response

It is designed to be easy to run locally and a good starting point for building more advanced document Q&A apps.

## Features

- Document ingestion from local files
- Text chunking and embedding generation
- Vector search for semantic retrieval
- Prompt-based answer generation using an LLM
- Simple project structure for experimentation and extension

## Tech Stack

- Python
- LangChain / similar RAG libraries (if used in the app)
- Vector database or in-memory embedding store
- OpenAI compatible LLM endpoint or local model backend

## Requirements

- Python 3.10+
- Miniconda or Anaconda (recommended for environment management)
- Access to an embedding model and LLM provider
- Optional: GPU support for faster local inference

## Install Python with Miniconda

1. Download and install Miniconda from the official site.
2. Create a new environment:

```bash
conda create -n mini-rag python=3.10
conda activate mini-rag
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Place your documents in a `data/` folder or configure the document source path in the app.
2. Update configuration values such as model names, embedding settings, and storage paths.
3. Run the app:

```bash
python app.py
```

## Usage

- Start the application.
- Upload or index documents.
- Ask a question based on the document content.
- Review the retrieved context and generated answer.

## Project Structure

```text
mini-rag-app/
├── app.py
├── requirements.txt
├── data/
├── README.md
└── src/
```

## Notes

This project is intended as a small educational or prototype RAG app. You can extend it with:

- web UI support
- better document parsing
- database-backed storage
- authentication and user management
- production deployment setup

## License

This project is provided for learning and experimentation. Add your preferred license if you plan to share or distribute it publicly.

