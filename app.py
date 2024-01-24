from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import db_login, db_password

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_login}:{db_password}@192.168.1.180:5432/postgres"
db = SQLAlchemy(app)


class Request(db.Model):
    __tablename__ = "Request"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cash_amount = db.Column(db.Float, nullable=False)
    card_number = db.Column(db.String(50), db.ForeignKey('Requisite.card_number'), nullable=False) # tODO что-то тут не так
    status = db.Column(db.String(16), nullable=False)
    requests = db.relationship("Requisite", backref="Request") # tODO что-то тут не так

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


if __name__ == "__main__":
    app.run()
