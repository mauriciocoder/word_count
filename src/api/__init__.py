import logging
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from .routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(bp)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Flask application initialized.")
    swagger_config = {
        "title": "Voxy - Word Count API",
        "version": "1.0.0",
        "description": "",
    }
    Swagger(app, config=swagger_config, merge=True)
    return app


app = create_app()
