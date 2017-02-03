from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static/')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'false'

db = SQLAlchemy(app)

@app.route('/')
def home_page():
    return render_template('base.html')

@app.route('/user/<nam>')
def profile_page(nam):
    return render_template('profile.html', name=nam)

if __name__=='__main__':
    app.run()
