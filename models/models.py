from extensions import db

class Link:
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
