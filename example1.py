from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hello():
<<<<<<< HEAD
    return 'Hello world..!!!'
=======
    return 'Hello world <b>python</b>'
>>>>>>> 86eab8b2a8b35d45c900644716096c883d579800

if __name__ == '__main__':
    app.run()
