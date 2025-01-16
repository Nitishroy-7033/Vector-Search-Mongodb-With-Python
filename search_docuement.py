import numpy as np
import torch
from scipy.spatial.distance import cosine

def search_similar(collection, query_text, model, tokenizer, top_k=5):
    """
    Search for similar documents based on a query text.
    
    Args:
        collection: MongoDB collection object.
        query_text: The input text to search for.
        model: Pretrained embedding model.
        tokenizer: Tokenizer for the embedding model.
        top_k: Number of top results to return.
    
    Returns:
        List of tuples with document text and similarity score.
    """
    # Generate embedding for the query text
    query_inputs = tokenizer(query_text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        query_embedding = model(**query_inputs).last_hidden_state.mean(dim=1).squeeze().numpy()

    # Fetch all documents from the collection
    cursor = collection.find({}, {"text": 1, "embedding": 1})
    results = []
    
    # Calculate similarity with each document
    for doc in cursor:
        doc_text = doc["text"]
        doc_embedding = np.array(doc["embedding"])  # Convert list back to numpy array
        similarity = 1 - cosine(query_embedding, doc_embedding)  # Cosine similarity
        results.append((doc_text, similarity))
    
    # Sort results by similarity score in descending order
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results[:top_k]
