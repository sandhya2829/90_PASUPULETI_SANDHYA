# AI Customer Service Agent (Telecom Support)
## Project Overview

This project focuses on building an AI-powered Customer Service Agent for a Telecommunications (Telco) support environment using Retrieval-Augmented Generation (RAG).
The system assists customer support teams by automating responses to frequently asked questions, guiding users through basic troubleshooting steps, and escalating complex issues to human agents when required.By leveraging Large Language Models (LLMs) together with a vector database of historical telecom support tickets and dialogue conversations, the system delivers accurate, context-aware, and consistent responses. This improves response time, reduces agent workload, and enhances customer satisfaction.

# Tools & Technologies
- Python – Core programming language for data processing, retrieval, and orchestration

- Pandas – Data loading and preprocessing of customer interaction datasets

- Sentence-Transformers – Generating semantic embeddings (all-MiniLM-L6-v2)

- ChromaDB – Vector database for storing and retrieving embeddings

- LangChain (Community) – Integration framework for embeddings, vector stores, and RAG pipeline

- Google Gemini API – Large Language Model used for context-aware answer generation

- Retrieval-Augmented Generation (RAG) – Architecture combining retrieval with LLM-based generation

- JSON – Structured format for final responses (answer, escalation flag, source IDs)

- VS Code / Command Line – Development and execution environment

# Datasets

The system uses publicly available and simulated telecom-related datasets:

Telecom Customer Support Dialogues (Kaggle) – customer–agent chat conversations

Telecom Support Tickets – issue descriptions, categories, and resolutions

Knowledge Base Articles – FAQs for billing, network issues, SIM problems, and plan upgrades

Dataset Link: https://www.kaggle.com/datasets/avinashok/telecomagentcustomerinteractiontext

# Step-by-Step Implementation Plan
## 1. Data Preparation

The raw telecom interaction dataset contains short and noisy customer messages along with multiple metadata fields. To prepare the data for a Retrieval-Augmented Generation (RAG) system, only essential columns such as the record ID, customer interaction text, and agent-assigned topic were selected, while irrelevant attributes were removed.

Each record was converted into a clear natural-language document by combining the customer message with its assigned issue category. Invalid or empty records were filtered out, and the processed documents were stored in a structured JSON format to enable efficient embedding generation and semantic retrieval.

## 2. Embeddings and Vector Database

- Preprocessed customer interaction documents were converted into semantic embeddings using a sentence-transformer model to capture the meaning of customer issues.

- The generated embeddings were stored in a Chroma vector database, which serves as the system’s memory for similarity-based retrieval.

- Relevant metadata such as record ID and issue category were stored along with embeddings to support traceability and explainable results.

- This step enables efficient semantic search and forms the core of the Retrieval-Augmented Generation (RAG) pipeline.

## 3. RAG Query Pipeline

- A user query is taken as input and converted into a vector embedding using the same embedding model used during indexing.

- The query embedding is compared against stored document embeddings in the Chroma vector database using semantic similarity search.

- The top relevant historical customer interaction records are retrieved based on similarity scores.

- Each retrieved result includes the processed text along with metadata such as record ID and issue category.

- The retrieved records provide contextual knowledge for the response generation stage of the RAG pipeline.

## 4. Escalation Rules & Human Handoff

The system determines when to escalate issues to human agents:

Confidence Threshold: Escalates if retrieval score is below a set threshold (e.g., < 0.7)

Keyword Triggers: Detects phrases like:

“I want to speak to a manager”

“Cancel my service”

“Legal action”
