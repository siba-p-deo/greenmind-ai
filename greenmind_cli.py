from agents.impulse_agent import ImpulseAgent
from agents.reflection_agent import ReflectionAgent
from agents.category_detector import CategoryDetector
import chromadb
from agents.alternatives_agent import AlternativesAgent

impulse_agent = ImpulseAgent()
reflection_agent = ReflectionAgent()
category_detector = CategoryDetector()
alternatives_agent = AlternativesAgent()

client = chromadb.PersistentClient(path="./db")
collection = client.get_collection("greenmind")

product = input(
    "What product do you want to buy?\n> "
)

reason = input(
    "Why do you want to buy it?\n> "
)

category = category_detector.detect(product)
alternatives = alternatives_agent.get_alternatives(category)

print("\nDetected Category:")
print(category)

answers = {
    "reason": reason
}

impulse_result = impulse_agent.classify(answers)

impulse_type = impulse_result["impulse_type"]
reasoning = impulse_result["reasoning"]

print("\nImpulse Type:")
print(impulse_type)

print("\nReasoning:")
print(reasoning)

result = collection.query(
    query_texts=[category],
    n_results=1
)

context = result["documents"][0][0]

print("\nRetrieved Category:")
print(result["ids"][0][0])

output = reflection_agent.generate(
    impulse_type,
    context
)

print("\nSuggested Alternatives:")

for item in alternatives:
    print(f"• {item}")

print(output)