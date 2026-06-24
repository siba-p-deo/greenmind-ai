from agents.impulse_agent import ImpulseAgent
from agents.reflection_agent import ReflectionAgent
import chromadb

# Initialize agents
impulse_agent = ImpulseAgent()
reflection_agent = ReflectionAgent()

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./db")
collection = client.get_collection("greenmind")

# User input
reason = input("Why do you want to buy this product?\n> ")

answers = {
    "reason": reason
}

# Step 1: Classify
impulse_type = impulse_agent.classify(answers)

# Step 2: Retrieve sustainability context
result = collection.query(
    query_texts=[reason],
    n_results=1
)

context = result["documents"][0][0]

# Step 3: Generate reflection
output = reflection_agent.generate(
    impulse_type,
    context
)

# Step 4: Display
print("\n" + "="*50)
print(output)
print("="*50)