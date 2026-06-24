# GreenMind AI - Model Card

## Model Details

**Model Name:** GreenMind AI v1.0  
**Model Type:** Multi-agent RAG system  
**Purpose:** Sustainability decision support for consumer purchases  
**Alignment:** UN SDG 12 (Responsible Consumption and Production)  
**Last Updated:** 2026-06-19

### Architecture Components

1. **Category Detector Agent**
   - Type: Rule-based keyword matching
   - Input: Product name (string)
   - Output: Category label (string)
   - Categories: 10 product types

2. **Impulse Agent**
   - Type: Rule-based classification
   - Input: Purchase reason (string)
   - Output: Impulse type (Necessity/Upgrade/Emotional/Comparison)
   - Method: Keyword pattern matching

3. **Reflection Agent**
   - Type: Template-based generation
   - Input: Impulse type + sustainability context
   - Output: Personalized reflection (string)
   - Method: Static templates with context injection

4. **RAG System**
   - Vector Database: ChromaDB
   - Embedding Model: Default (sentence-transformers)
   - Knowledge Base: 10 curated markdown documents
   - Retrieval: Semantic similarity search

## Intended Use

### Primary Use Cases
- Help consumers make informed sustainable purchasing decisions
- Provide category-specific sustainability information
- Encourage reflection before impulse purchases
- Raise awareness of environmental impact

### Out-of-Scope Use Cases
- Financial advice or investment recommendations
- Medical or health-related purchase decisions
- Legal compliance or regulatory guidance
- Commercial product recommendations

## Training Data

### Knowledge Base
- **Source:** Curated sustainability research and guidelines
- **Size:** 10 documents covering major consumer categories
- **Format:** Markdown files with structured sections
- **Update Frequency:** Manual updates as needed
- **Language:** English only

### Categories Covered
1. Smartphones
2. Laptops
3. Fast Fashion
4. Shoes
5. Headphones/Audio
6. Gaming Accessories
7. Watches/Wearables
8. Self-Care Products
9. Furniture
10. Home Appliances

## Performance Metrics

### Current Performance (as of v1.0)
- **Category Detection Accuracy:** ~85% (estimated, needs formal evaluation)
- **Impulse Classification:** Rule-based (no accuracy metric)
- **User Satisfaction:** Not yet measured
- **Response Time:** <2 seconds average

### Known Limitations
- Limited to 10 product categories
- No confidence scores provided
- Rule-based classification may miss nuanced cases
- English language only
- No personalization

## Ethical Considerations

### Fairness & Bias
**Potential Biases:**
- Economic bias: May not account for budget constraints
- Cultural bias: Western-centric sustainability perspectives
- Language bias: English-only interface

**Mitigation Efforts:**
- Avoid judgmental language in classifications
- Provide context-aware advice
- Plan to add multi-language support

### Privacy & Data Protection
**Current State:**
- User inputs logged for improvement
- No personal identifiers collected
- Local database storage only

**Planned Improvements:**
- Add explicit user consent
- Implement data retention policy (30 days)
- Add anonymization for logged data

### Transparency & Explainability
**Current State:**
- Category detection shown to user
- Impulse type classification displayed
- Source documents identified

**Planned Improvements:**
- Add confidence scores
- Explain reasoning for classifications
- Provide source attribution for facts

## Limitations & Risks

### Technical Limitations
1. **Limited Categories:** Only 10 product types covered
2. **Rule-Based Logic:** May miss edge cases and nuanced situations
3. **No Confidence Scores:** Cannot express uncertainty
4. **Static Knowledge:** Requires manual updates
5. **Single Language:** English only

### Operational Risks
1. **Incorrect Categorization:** May provide irrelevant advice
2. **Outdated Information:** Knowledge base may become stale
3. **User Misinterpretation:** Advice may be misunderstood
4. **Over-Reliance:** Users may defer all decisions to system

### Mitigation Strategies
- Regular knowledge base updates
- User feedback collection
- Clear disclaimers about limitations
- Encourage critical thinking

## Recommendations

### For Users
- Use as a decision support tool, not a replacement for judgment
- Consider personal circumstances and constraints
- Verify sustainability claims independently
- Provide feedback for improvement

### For Developers
- Expand category coverage
- Implement ML-based classification
- Add confidence scoring
- Conduct formal bias testing
- Implement user feedback loop

## Maintenance & Updates

### Update Schedule
- Knowledge base: Quarterly review
- Model improvements: Continuous
- Security patches: As needed

### Version History
- v1.0 (2026-06-19): Initial release with 10 categories

## Contact & Feedback

Source Code Repository:
https://github.com/siba-p-deo/greenmind-ai

For questions, feedback, or to report issues:
- GitHub Issues: https://github.com/siba-p-deo
- Email: siba.p.deo@gmail.com

## References

1. UN Sustainable Development Goal 12: Responsible Consumption and Production
2. Circular Economy Principles
3. Product Lifecycle Assessment Standards
4. Behavioral Economics Research on Impulse Purchasing

---

**Disclaimer:** GreenMind AI provides general sustainability guidance based on category-level information. It does not replace professional advice or personal judgment. Users should consider their individual circumstances when making purchasing decisions.