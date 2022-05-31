from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(type_=db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(name='first_name', type_=db.String(20), default='John')
    last_name = db.Column(name='last_name', type_=db.String(20), default='Doe')
    title = db.Column(name='title', type_=db.String(20))
    mobile = db.Column(name='mobile', type_=db.String(10))
    email = db.Column(name='email', type_=db.String(120))
    avatar = db.Column(name='avatar', type_=db.Text, comment='avatar url')

    def __init__(self, first_name, last_name, title=None, mobile=None, email=None, avatar=None):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.mobile = mobile
        self.email = email
        self.avatar = avatar

    def __repr__(self):
        return f'<User {self.first_name!r}>'
