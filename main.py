from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), unique=True)
    content = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

new_user = User(
    user="admin",
    email="slush@lol.de",
    password="Test123"
)

@app.route("/")
def welcome():
    users = User.query.all()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
