from application import db
from flask_login import UserMixin
from application import login_manager
from datetime import date, datetime
from itsdangerous import URLSafeSerializer
import uuid


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    share_token = db.Column(db.String(64), unique=True, nullable=True)
    sharing_enabled = db.Column(db.Boolean, default=False)

    moods = db.relationship('MoodEntry', backref='user', lazy=True)

    def generate_share_token(self):
        self.share_token = uuid.uuid4().hex
        db.session.commit()


class MoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.String(50), nullable=False)
    intensity = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False, default=date.today)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    tags = db.Column(db.String(200))
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class UserTriggerCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    __table_args__ = (db.UniqueConstraint('category', 'user_id', name='user_cat_uc'),)