from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class random(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamb = db.Column(db.DateTime)
    value = db.Column(db.Integer)

    def __repr__(self):
        return 'random(id=%s, time_stamb=%s, value=%s)' % (self.id, self.time_stamb, self.value)
