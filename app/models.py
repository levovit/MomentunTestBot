from app import db


class User(db.Model):
    __tablename__ = "User"
    telegram_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    def __repr__(self):
        return f"{self.name} - {self.age}"
