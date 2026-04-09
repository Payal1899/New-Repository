
#create Flask api with routes to pages, use render template to goto html Form page
#create a html file with post method and HTML form with submit button, define action for submit to come to api page
#Get data from user
#create a db user in mongo db, in network access give your public ip address so that you may connect to db with this machine
#Goto cluster and click connect>connect to your application>>do basic settings and done
#you will receive URI paste it in .env(separately created file) to secure creds
#created requirements.txt for all the required import pckgs
#run command pip install -r requirements.txt to install all of them

from flask import Flask, render_template, request #request and jsonify is flask func
import requests  #this is python lib to connect https requests

Backend_URL='http://0.0.0.0:8000'
app= Flask(__name__) #creating flask 
@app.route('/')
def first_fun():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def sec_fun():
    dict1=dict(request.form)
    requests.post(Backend_URL+'/submit', json=dict1) #we have var name json but in backend we are taking data as dict1=dict(request.form)
    #hence in backend change it to dict1=dict(request.json) otherwise it will accept data but dont save in DB
    #it gives result "http://127.0.0.1:5000/submit" and passed dict1
    return 'data inserted successful'


@app.route('/get_Data') #(/view_Data is just kept to keep it similar name, you can give anything)
def thrid_fun():
    response=requests.get(Backend_URL+'/view_Data') #here /view_Data is the route defind in backend
    return response.json() #provides output in json



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)  #running frontend and backend on different ports