from app import db


class User(db.Model):
    telegram_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), default="Anon")
    age = db.Column(db.Integer, default=0)
    gender = db.Column(db.String(20), default="")
    state = db.Column(db.String(15), default="name")

    def __repr__(self):
        return f"{self.name} - {self.age}"

    @classmethod
    def get_state_by_id(cls, telegram_id):
        user = cls.query.filter_by(telegram_id=telegram_id).first()
        if user:
            return user.state
        else:
            return False
