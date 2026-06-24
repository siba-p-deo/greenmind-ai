"""Input validation and sanitization utilities."""

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_user_input(text: str, max_length: int = 500, min_length: int = 1) -> str:
    """
    Validate and sanitize user input.
    
    Args:
        text: User input string
        max_length: Maximum allowed length
        min_length: Minimum required length
    
    Returns:
        Sanitized input string
    
    Raises:
        ValidationError: If input is invalid
    """
    if not text or not isinstance(text, str):
        raise ValidationError("Input must be a non-empty string")
    
    text = text.strip()
    
    if len(text) < min_length:
        raise ValidationError(f"Input too short (minimum {min_length} characters)")
    
    if len(text) > max_length:
        raise ValidationError(f"Input too long (maximum {max_length} characters)")
    
    return text

def safe_query_chromadb(collection, query_text: str, n_results: int = 1) -> dict:
    """
    Safely query ChromaDB with error handling.
    
    Args:
        collection: ChromaDB collection
        query_text: Query string
        n_results: Number of results to retrieve
    
    Returns:
        Query results or empty structure if query fails
    """
    try:
        result = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        
        # Validate results
        if not result or not result.get("documents") or not result["documents"][0]:
            return {
                "documents": [["No sustainability data available for this category."]],
                "ids": [["fallback"]],
                "metadatas": [[{"category": "unknown"}]]
            }
        
        return result
    
    except Exception as e:
        print(f"Warning: ChromaDB query failed: {e}")
        return {
            "documents": [["Unable to retrieve sustainability information at this time."]],
            "ids": [["error"]],
            "metadatas": [[{"category": "error"}]]
        }