import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.hw

with open('quotes.json', 'r', encoding='utf-8') as quotes_file:
    quotes = json.load(quotes_file)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    
    if author:
        db.quotes.insert_one({
        'author': ObjectId(author['_id']),
        'quote': quote['quote'],
        'tags': quote['tags']
})
        
       