from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo

load_dotenv() #calling function to load uri stored in .env file
MONGO_URI = os.getenv('uri') # same variable which is passed in .env file
client = pymongo.MongoClient(MONGO_URI)#created a client by providing the URI

db = client.Assignment2 #created DB named 'Assignment2' in cluster name mentioned in URI

collection = db['Assignment']#created collection named 'Assignment'

app= Flask(__name__) #creating flask api

@app.route('/submit', methods=['POST'])
def sec_fun():
    #inserting into DB
    dict1=dict(request.json)
    collection.insert_one(dict1)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True) #running frontend and backend on different ports