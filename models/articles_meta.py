from app import db


class ArticleMeta(db.Model):
    __tablename__ = 'articles_meta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(name='content', type_=db.Text)
    article_id = db.Column(name='article_id', type_=db.Integer)

    def __init__(self, content=None, article_id=None):
        self.content = content
        self.article_id = article_id

    def __repr__(self):
        return f'<Article meta name is {self.article_id!r}>'
