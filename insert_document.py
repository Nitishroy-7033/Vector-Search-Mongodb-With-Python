from pymongo import errors

def insert_document(collection, text, embedding):
    try:
        document = {
            "text": text,
            "embedding": embedding.tolist()  # Convert numpy array to list
        }
        collection.insert_one(document)
        print("Document inserted successfully!")
    except errors.PyMongoError as e:
        print("An error occurred while inserting the document.")
        print(f"Details: {e}")