from mongo_connection import connect_to_mongo
from embedding_generator import get_embedding
from insert_document import insert_document
from search_docuement import search_similar
from transformers import AutoTokenizer, AutoModel

# MongoDB URI and details
mongo_uri = "mongodb+srv://mrnitishkrs:LM7wP0LG9CIAR39U@database.k8efh.mongodb.net"
db_name = "learning"
collection_name = "messages"

# Connect to MongoDB
collection = connect_to_mongo(mongo_uri, db_name, collection_name)


# Text to embed
# text = "Cloud computing has transformed the way businesses handle data and scalability."

# Generate the embedding
# embedding = get_embedding(text)

# print(embedding)
# Insert the document
# insert_document(collection, text, embedding)



# Search Document 
# Example query text

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

query_text = "How can AI transform industries?"

# Perform the search
results = search_similar(collection, query_text, model, tokenizer, top_k=3)

# Print the results
for text, similarity in results:
    print(f"Text: {text}\nSimilarity: {similarity:.4f}\n")
