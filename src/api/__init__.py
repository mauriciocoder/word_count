import logging
from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from .routes import bp


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)  # Enable CORS globally for all routes
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


# Since FLASK_APP=src/api is set in docker-compose.yml
# It is required to instantiate the Flask src here (src)
app = create_app()
