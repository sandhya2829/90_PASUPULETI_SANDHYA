import pandas as pd
import json
import os

# Paths
DATA_PATH = r"C:\Users\22nn1\OneDrive\Attachments\Desktop\VU Hackthon\CustomerInteractionData.csv"
OUTPUT_PATH = "ingestion/processed_docs.json"

def preprocess_data():
    df = pd.read_csv(DATA_PATH)

    documents = []

    for _, row in df.iterrows():
        record_id = row["RecordID"]
        customer_text = str(row["CustomerInteractionRawText"]).strip()
        topic = str(row["AgentAssignedTopic"]).strip()

        # Skip empty or invalid text
        if customer_text == "" or customer_text.lower() == "nan":
            continue

        text = (
            f"Customer reported the following issue: {customer_text}. "
            f"The issue is categorized under {topic}."
        )

        doc = {
            "record_id": int(record_id),
            "text": text,
            "category": topic
        }

        documents.append(doc)

    os.makedirs("ingestion", exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(documents, f, indent=2)

    print(f"Preprocessing completed successfully. {len(documents)} documents created.")

if __name__ == "__main__":
    preprocess_data()
