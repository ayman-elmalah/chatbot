from app import db

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # 'user' or 'ai'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
