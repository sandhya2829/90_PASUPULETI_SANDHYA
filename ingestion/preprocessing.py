import sys
import os
import google.generativeai as genai

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

genai.configure(api_key="AIzaSyBaXVO4uJ0ePQiKIhyc6w5qCW_452_7hhU")
model = genai.GenerativeModel("gemini-pro")

def generate_answer(query, retrieved_docs):
    if not retrieved_docs:
        return None   # let step 6 handle escalation

    context = "\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are a telecom customer support assistant.

Use the following past customer support records to answer the question.
Provide a clear and helpful response.

Context:
{context}

Customer Question:
{query}

Answer:
"""

    response = model.generate_content(prompt)
    return response.text.strip()

