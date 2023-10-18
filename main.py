from src.controllers.extraction_controller import extraction_blueprint
from flask import Flask
from src.services.extraction_service import ExtractionService
from config import setup_logging
from flask import Flask
from flask_cors import CORS

setup_logging()

service = ExtractionService()
app = Flask(__name__)
app.register_blueprint(extraction_blueprint, url_prefix="/api")
CORS(app)

if __name__ == "__main__":
    app.run()
