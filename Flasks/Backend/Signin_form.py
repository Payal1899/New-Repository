
#create Flask api with #routes to pages, use render template to goto html Form page
#create a html file with post method and HTML form with submit button, define action for submit to come to api page
#Get data from user
#create a db user in mongo db, in network access give your public ip address so that you may connect to db with this machine
#Goto cluster and click connect>connect to your application>>do basic settings and done
#you will receive URI paste it in .env(separately created file) to secure creds
#created requirements.txt for all the required import pckgs
#run command pip install -r requirements.txt to install all of them

from flask import Flask, request,jsonify #request and jsonify is flask func
from dotenv import load_dotenv
import os
import pymongo

load_dotenv() #calling function to load uri stored in .env file
MONGO_URI = os.getenv('uri') # same variable which is passed in .env file
client = pymongo.MongoClient(MONGO_URI)#created a client by providing the URI

db = client.test#created DB named 'test' in cluster name mentioned in URI

collection = db['flask-tutorial']#created collection named 'flask-tutorial'

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


app= Flask(__name__) #creating flask 

@app.route('/submit', methods=['POST'])
def sec_fun():
    #inserting into DB
    dict1=dict(request.json)
    collection.insert_one(dict1) #inserting data into our DB using collection
    return 'Data inserted successfully'

@app.route('/view_Data')
def thrid_fun():

    data=collection.find()
    data=list(data)
    print(data) #output once we convert to list [{'_id': ObjectId('69cfe05373a01b79560a3400'), 'name': 'Punam', 'email': 'iloveyou@gmail.com', 'password': '1245', 'confirm_password': '1245'},{},{} and go on]
    #as it is giving _id also and we do not need that in output, we are deleting it
    for item in data:
        print("item>>",item) 
        del item['_id']
        print("item after deleting ID>>",item) 
        dat1={
            'Key':data  
            # as we converted 'data' which is cursor we fetched from DB to list now we are creating dict
            #created dict dat1 and alligned key with list>'data' in our case. now we can return this dict
        }

    return jsonify(dat1) #providing json version of output


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000, debug=True) #running frontend and backend on different ports