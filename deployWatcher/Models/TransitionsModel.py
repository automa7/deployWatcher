from datetime import datetime
from deployWatcher.database import db

class TransitionModel(db.Model):
    __tablename__ = 'Transitions'

    id = db.Column(db.Integer, primary_key=True)
    component = db.Column(db.String(140))
    version = db.Column(db.Float(precision=2))
    author = db.Column(db.String(80))
    status = db.Column(db.String(50))
    sentTimestamp = db.Column(db.DateTime)
    receivedTimestamp = db.Column(db.DateTime)

    def __init__(self, component: str, version: float, author: str, status: str,
                 sent_timestamp: str = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')):
        self.component = component
        self.version = version
        self.author = author
        self.status = status
        self.sentTimestamp = datetime.strptime(sent_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        self.receivedTimestamp = datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()
