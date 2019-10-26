from flask import Flask
from backend.data import alchemy, migrate
from backend.controller import main


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    # Extensions
    alchemy.configure(app)
    migrate.configure(app)

    # Blueprints
    main.configure(app)

    return app
