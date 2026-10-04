from flask import Flask
from flask_cors import CORS

from config import Config
from routes.health import health_bp
from routes.db_test import db_bp
from routes.article_test import article_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

app.register_blueprint(health_bp)
app.register_blueprint(db_bp)
app.register_blueprint(article_bp)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=Config.PORT,
        debug=True
    )