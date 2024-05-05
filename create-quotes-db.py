# Create a Mongita database with movie information
import json
from mongita import MongitaClientDisk

quotes_data = [
    {"text": "I'm hungry. When's lunch?", "author": "Dorothy","owner":"Greg"},
    {"text": "You threw that ball. You go get it.", "author": "Suzy", "owner":"Dorothy"},
]

# create a mongita client connection
client = MongitaClientDisk()

# create a movie database
quotes_db = client.quotes_db

# create a quotes collection
quotes_collection = quotes_db.quotes_collection

# empty the collection
quotes_collection.delete_many({})

# put the quotes in the database
quotes_collection.insert_many(quotes_data)

# make sure the quotes are there
print(quotes_collection.count_documents({}))
