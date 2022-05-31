import os

from flask import Flask
from flask import request, Response
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import basedir
from mailer.mailer import create_email

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.normpath(os.path.join(basedir, app.config.get("DB")))}'
db = SQLAlchemy(app)

from models.models import *

mail = Mail(app)


@app.route('/message', methods=["POST"])
def message():
    try:
        data = request.json
        mail_template = create_email(name=data["name"], phone=data["phone"])
        mail.send(mail_template)
        response = Response(status=200)
        return response
    except Exception as err:
        response = Response(response=str(err), status=500)
        return response


@app.route('/tips/<string:tip_id>', methods=["GET"])
def get_article(tip_id):
    with app.app_context():
        try:
            u = User(first_name='John', last_name='Smith')
            am = ArticleMeta()
            a = Article(meta=am, author=u)
            a.meta = am
            a.author = u
            s = db.session()
            s.add(a)
            s.add(u)
            s.add(am)
            s.commit()
            response = Response(status=200)
            return response
        except Exception as err:
            response = Response(response=str(err), status=500)
            return response


if __name__ == '__main__':
    app.debug = True
    app.run()
