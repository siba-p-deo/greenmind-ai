import os
import chromadb

client = chromadb.PersistentClient(path="./db")

collection = client.get_or_create_collection(
    name="greenmind"
)

folder = "knowledge_base"

for file in os.listdir(folder):

    if file.endswith(".md"):

        path = os.path.join(folder, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        collection.add(
            documents=[text],
            ids=[file],
            metadatas=[
                {
                    "category": file.replace(".md", "")
                }
            ]
        )

print("Documents Added")