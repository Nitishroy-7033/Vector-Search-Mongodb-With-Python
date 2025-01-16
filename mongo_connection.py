from pymongo import MongoClient, errors
import sys

def connect_to_mongo(uri, db_name, collection_name):
    try:
        # Attempt to connect to MongoDB
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # Set a timeout for the connection
        client.server_info()  # Trigger server selection to confirm connection
        print("Connected to MongoDB successfully!")
        db = client[db_name]
        collection = db[collection_name]
        return collection
    except errors.ServerSelectionTimeoutError as e:
        print("Error: Unable to connect to MongoDB. Check your connection string or network settings.")
        print(f"Details: {e}")
        sys.exit(1)
    except errors.PyMongoError as e:
        print("A MongoDB error occurred.")
        print(f"Details: {e}")
        sys.exit(1)