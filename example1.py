from flask import Flask 
app = Flask(__name__)

@app.route('/hello')
def hello():
<<<<<<< HEAD
    return 'Hello world...!!!'
=======
    return 'Hello world <b>python</b>'
>>>>>>> e85f3cd1422a9fdbab2a13c97f19079d6b446361

if __name__ == '__main__':
    app.run()
