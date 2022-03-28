from sqlalchemy import JSON, VARCHAR
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class KVPair(db.Model):
    __tablename__ = 'kvpairs'
    identifier = db.Column(VARCHAR(length=36), primary_key=True, index=True, nullable=False)
    doc = db.Column(JSON(), nullable=False)

    def __init__(self, identifier, doc):
        self.identifier = identifier
        self.doc = doc
