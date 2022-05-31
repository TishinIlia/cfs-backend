from app import db


class ArticleMeta(db.Model):
    __tablename__ = 'article_meta'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(name='content', type_=db.Text, default='')

    # def __init__(self, content=None):
    #     self.content = content

    def __repr__(self):
        return f'<Article meta here>'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(type_=db.Integer, primary_key=True)
    first_name = db.Column(name='first_name', type_=db.String(20), nullable=False)
    last_name = db.Column(name='last_name', type_=db.String(20), nullable=False)

    # title = db.Column(name='title', type_=db.String(20))
    # mobile = db.Column(name='mobile', type_=db.String(10))
    # email = db.Column(name='email', type_=db.String(120))
    # avatar = db.Column(name='avatar', type_=db.Text, comment='avatar url')

    # def __init__(self, first_name, last_name, title=None, mobile=None, email=None, avatar=None):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.title = title
    #     self.mobile = mobile
    #     self.email = email
    #     self.avatar = avatar

    def __repr__(self):
        return f'<User {self.first_name!r}>'


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    meta_id = db.Column(db.ForeignKey('meta.id'), name='meta_id', nullable=False)
    meta = db.relationship('ArticleMeta', backref=db.backref('article'))
    # title = db.Column(name='title', type_=db.String(255), default='', nullable=False)
    # meta_title = db.Column(name='meta_title', type_=db.Integer)
    # slug = db.Column(name='slug', type_=db.String(32))
    # summary = db.Column(name='summary', type_=db.String(255))
    # content = db.Column(name='content', type_=db.Text)
    # created_at = db.Column(name='created_at', type_=db.String, nullable=False, default=datetime.now(timezone.utc))
    author_id = db.Column(db.ForeignKey('author.id'), name='author_id', nullable=False)
    author = db.relationship('User', backref=db.backref('article'))

    # main_image = db.Column(name='main_image', type_=db.Text)

    # def __init__(
    #         self,
    #         title,
    #         created_at,
    #         meta_id,
    #         meta,
    #         meta_title=None,
    #         slug=None,
    #         summary=None,
    #         content=None,
    #         author_id=None,
    #         main_image=None
    # ):
    #     self.title = title
    #     self.meta_title = meta_title
    #     self.meta = meta
    #     self.meta_id = meta_id
    #     self.slug = slug
    #     self.summary = summary
    #     self.content = content
    #     self.created_at = datetime.fromtimestamp(created_at, timezone.utc)
    #     self.author_id = author_id
    #     self.main_image = main_image

    def __repr__(self):
        return f'<Article name is {self.created_at!r}>'
