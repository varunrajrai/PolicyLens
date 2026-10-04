from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from routes.auth import auth
from utils.auth import bcrypt


app = Flask(__name__)
from routes.citizen import citizen_bp
CORS(app)

# -------------------------
# Bcrypt
# -------------------------
bcrypt.init_app(app)

# -------------------------
# JWT Configuration
# -------------------------
app.config["JWT_SECRET_KEY"] = "your_super_secret_key"

jwt = JWTManager(app)

# -------------------------
# Register Blueprints
# -------------------------
app.register_blueprint(auth)

app.register_blueprint(
    citizen_bp,
    url_prefix="/citizen"
)


@app.route("/")
def home():
    return jsonify({
        "message": "Backend is running"
    })



if __name__ == "__main__":
    app.run(debug=True)