from app import db

class Setting(db.Model):
    __tablename__ = 'settings'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Setting {self.key}={self.value}>"

    @staticmethod
    def get_value(key):
        """Retrieve a setting value by key."""
        setting = Setting.query.filter_by(key=key).first()
        if setting:
            return setting.value
        return None

    @staticmethod
    def set_value(key, value):
        """Set or update a setting by key."""
        setting = Setting.query.filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            setting = Setting(key=key, value=value)
            db.session.add(setting)
        db.session.commit()
