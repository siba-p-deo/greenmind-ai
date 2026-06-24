# GreenMind AI

GreenMind AI is an AI-powered sustainability decision-support assistant designed to help consumers make more thoughtful purchasing decisions.

The project aligns with **United Nations Sustainable Development Goal 12 (Responsible Consumption and Production)** by encouraging users to reflect on their purchasing motivations before buying products.

---

# Problem Statement

Modern consumer culture encourages frequent upgrades, impulse purchases, and trend-driven consumption.

Many consumers are unaware of the environmental impact associated with product manufacturing, short replacement cycles, and electronic waste.

GreenMind AI addresses this challenge by combining:

- Purchase intent analysis
- Sustainability knowledge retrieval
- Reflection-based decision support

to encourage more conscious consumption.

---

# Features

## Category Detection

Automatically identifies product categories including:

- Smartphones
- Laptops
- Fast Fashion
- Shoes
- Headphones
- Gaming Accessories
- Watches
- Self-Care Products
- Furniture
- Home Appliances

---

## Impulse Analysis

Classifies purchasing motivations into:

- Necessity
- Upgrade
- Emotional
- Comparison

---

## Sustainability Context Retrieval

Uses ChromaDB and Retrieval-Augmented Generation (RAG) principles to retrieve category-specific sustainability information.

---

## Reflection Engine

Provides contextual sustainability reflections to encourage thoughtful decision-making.

---

# Technology Stack

- Python
- ChromaDB
- Sentence Transformers
- Markdown Knowledge Base
- Retrieval-Augmented Generation (RAG)
- IBM Granite (Project Review and Refinement)
- GitHub

---

# Installation

## Clone Repository

```bash
git clone <repository-link>
cd greenmind
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Build Knowledge Base

```bash
python build_db.py
```

---

# Run GreenMind

```bash
python greenmind_cli.py
```

---

# Example

Input:

Product:
iPhone

Reason:
Better camera and new features

Output:

Detected Category:
Smartphones

Impulse Type:
Upgrade

Sustainability Context:
[Retrieved category-level sustainability information]

Reflection:
Your motivation appears driven by feature improvements rather than product failure. Consider whether your current device still meets your needs before upgrading.

---

# Project Structure

```text
greenmind/
│
├── greenmind_cli.py
├── build_db.py
│
├── agents/
│   ├── category_detector.py
│   ├── impulse_agent.py
│   └── reflection_agent.py
│
├── knowledge_base/
│   ├── smartphones.md
│   ├── laptops.md
│   └── ...
│
├── db/
│
├── README.md
├── MODEL_CARD.md
└── ARCHITECTURE.md
```

---

# Responsible AI

GreenMind AI:

- Provides category-level information only
- Avoids unsupported environmental claims
- Does not provide financial or medical advice
- Encourages user judgment rather than replacing it

---

# SDG Alignment

Primary SDG:

**SDG 12 — Responsible Consumption and Production**

Secondary Contributions:

- SDG 13 — Climate Action
- SDG 11 — Sustainable Cities and Communities

---

# Future Improvements

- IBM Granite Integration
- Confidence Scores
- Web Interface
- Additional Product Categories
- Multi-Language Support

---

# License

Educational Project – 1M1B AI for Sustainability Internship