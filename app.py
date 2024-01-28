from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import db_login, db_password, db_host, db_port, db_name

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_login}:{db_password}@{db_host}:{db_port}/{db_name}"
db = SQLAlchemy(app)


class Request(db.Model):
    __tablename__ = "Request"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cash_amount = db.Column(db.Float, nullable=False)
    card_number = db.Column(db.String(50), db.ForeignKey('Requisite.card_number'), nullable=False)
    status = db.Column(db.String(16), nullable=False)
    requests = db.relationship("Requisite", backref="Request")

class Requisite(db.Model):
    __tablename__ = "Requisite"
    card_number = db.Column(db.String(50), primary_key=True)
    card_type = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    telephone_number = db.Column(db.String(50), nullable=False)
    limit = db.Column(db.Float, nullable=False)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/create")
def create():
    db.create_all()
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
