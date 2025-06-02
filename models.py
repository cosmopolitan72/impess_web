from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fcuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(64), unique=True, nullable=False) #사용자 id, 중복 불가, 빈칸 안된다.. 
    username = db.Column(db.String(64), nullable=False) 
    password = db.Column(db.String(128), nullable=False)
