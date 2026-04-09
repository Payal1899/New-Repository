#creating flask application

from flask import Flask
app= Flask(__name__) #creating flask application
@app.route('/') #/ means homepage
def home():
    return 'Hello Paya!'

#calling App
if __name__ == '__main__':
    app.run()
