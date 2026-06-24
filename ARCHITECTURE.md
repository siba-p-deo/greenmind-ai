# GreenMind AI Architecture

## Overview

GreenMind AI is a sustainability-focused decision support system that combines rule-based reasoning with Retrieval-Augmented Generation (RAG) principles.

The system analyzes a user's intended purchase, retrieves sustainability information, and generates reflective guidance before purchase decisions are made.

---

# High-Level Architecture

```text
User Input
    │
    ▼
Category Detector
    │
    ▼
Impulse Agent
    │
    ▼
ChromaDB Retrieval
    │
    ▼
Reflection Agent
    │
    ▼
Structured Advisory Response
```

---

# Layer 1 — User Interaction Layer

Responsible for collecting:

- Product Name
- Purchase Reason

Current Interface:

- Python CLI

Future Interface:

- Web Application

---

# Layer 2 — Decision Layer

## Category Detector

Purpose:

Identify the correct product category.

Method:

Rule-based keyword matching.

Example:

```text
iPhone → Smartphones
MacBook → Laptops
Facewash → Self-Care Products
```

---

## Impulse Agent

Purpose:

Analyze purchase motivation.

Classification Types:

- Necessity
- Upgrade
- Emotional
- Comparison

Current Method:

Rule-based pattern matching.

Future Enhancement:

IBM Granite-based classification.

---

# Layer 3 — Knowledge Retrieval Layer

## ChromaDB

Purpose:

Store vectorized sustainability knowledge.

Functions:

- Embedding Storage
- Similarity Search
- Document Retrieval

---

## Knowledge Base

Format:

Markdown Documents

Categories:

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

# Layer 4 — Reflection Layer

## Reflection Agent

Purpose:

Generate sustainability-oriented reflections.

Inputs:

- Impulse Type
- Retrieved Sustainability Context

Outputs:

- Reflective Guidance
- Sustainability Awareness

Current Method:

Template-Based Generation

Future Enhancement:

Granite-Assisted Reflection Generation

---

# Design Decisions

## Why Rule-Based Classification?

Benefits:

- Transparent
- Explainable
- Fast
- No Training Data Required

---

## Why ChromaDB?

Benefits:

- Lightweight
- Easy Local Deployment
- Efficient Semantic Retrieval

---

## Why Category-Level Sustainability Data?

Reason:

Product-specific sustainability claims are difficult to verify reliably.

Category-level guidance reduces misinformation risk and improves Responsible AI compliance.

---

# Responsible AI Design

GreenMind follows four principles:

## Transparency

Users can see:

- Detected Category
- Impulse Type

---

## Explainability

All decisions originate from visible rules and retrieved documents.

---

## Reliability

Knowledge comes from curated sustainability resources.

---

## Human Oversight

Users retain final decision-making authority.

GreenMind provides guidance only.

---

# Future Architecture

```text
User
 │
 ▼
Orchestrator Agent
 │
 ├── Category Agent
 ├── Impulse Agent
 ├── Sustainability Agent
 └── Reflection Agent
 │
 ▼
IBM Granite
 │
 ▼
Final Advisory Response
```

---

# Architecture Summary

GreenMind AI combines:

- Rule-Based Decision Systems
- Retrieval-Augmented Generation (RAG)
- Sustainability Knowledge Retrieval
- Responsible AI Principles

to promote more conscious consumer behavior and support SDG 12 objectives.