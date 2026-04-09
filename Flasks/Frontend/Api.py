from flask import Flask, render_template, request, redirect, url_for
import requests  #this is python lib to connect https requests

Backend_URL='http://0.0.0.0:8000'
app= Flask(__name__) #creating flask 
@app.route('/', methods=['GET','POST'])
def first_fun():
    if request.method=='POST':
        dict1=dict(request.form)
        if not dict1.get('name') or not dict1.get('email'):
            return render_template('index.html', error="All fields required")
                
        else:
            requests.post(Backend_URL+'/submit', json=dict1) 
            return redirect(url_for('sec_fun'))
    
    return render_template('index.html')
@app.route('/Submit')
def sec_fun():
    return 'Data submitted successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6000, debug=True)  #running frontend and backend on different ports