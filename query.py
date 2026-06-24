import chromadb

client = chromadb.PersistentClient(path="./db")

collection = client.get_collection(
    name="greenmind"
)

query = input("Enter query: ")

result = collection.query(
    query_texts=[query],
    n_results=3
)

print("\nTop Results:")

for i, doc_id in enumerate(result["ids"][0]):
    print(f"{i+1}. {doc_id}")