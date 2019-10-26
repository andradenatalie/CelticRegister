from flask_sqlalchemy import SQLAlchemy

alchemy = SQLAlchemy()


def configure(app):
    alchemy.init_app(app)
    app.db = alchemy
