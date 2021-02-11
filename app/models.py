from app import db


class UserText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))


    def __repr__(self):
        return f' {self.id} '


