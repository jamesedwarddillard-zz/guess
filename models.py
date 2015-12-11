from app import db
# from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    jobs = db.Column(db.Integer)

    def __init__(self, month, year, jobs):
        self.month = month
        self.year = year
        self.jobs = jobs

    def __repr__(self):
        return '<id {}>'.format(self.id)
