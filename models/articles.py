from datetime import datetime, timezone

from app import db


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(name='title', type_=db.String(255), default='', nullable=False)
    meta_title = db.Column(name='meta_title', type_=db.Integer)
    slug = db.Column(name='slug', type_=db.String(32))
    summary = db.Column(name='summary', type_=db.String(255))
    content = db.Column(name='content', type_=db.Text)
    created_at = db.Column(name='created_at', type_=db.String, nullable=False, default=datetime.now(timezone.utc))
    author_id = db.Column(name='author_id', type_=db.Integer)
    main_image = db.Column(name='main_image', type_=db.Text)

    def __init__(
            self,
            title,
            created_at,
            meta_title=None,
            slug=None,
            summary=None,
            content=None,
            author_id=None,
            main_image=None
    ):
        self.title = title
        self.meta_title = meta_title
        self.slug = slug
        self.summary = summary
        self.content = content
        self.created_at = datetime.fromtimestamp(created_at, timezone.utc)
        self.author_id = author_id
        self.main_image = main_image

    def __repr__(self):
        return f'<Article name is {self.created_at!r}>'
