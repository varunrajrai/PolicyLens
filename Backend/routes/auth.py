from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from models.db import get_db_connection
from utils.auth import bcrypt

auth = Blueprint("auth", __name__)


@auth.route("/test-db")
def test_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        database = cursor.fetchone()
        cursor.close()
        connection.close()

        return jsonify({
            "message": "Database Connected Successfully",
            "database": database[0]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@auth.route("/signup", methods=["POST"])
def signup():

    data = request.get_json() or {}

    full_name = data.get("full_name")
    email = data.get("email")
    password = data.get("password")
    role = (data.get("role") or "").upper()
    department = data.get("department")

    if not full_name or not email or not password or not role:
        return jsonify({
            "success": False,
            "message": "All fields are required."
        }), 400

    if role not in ["CITIZEN", "GOVERNMENT_ADMIN"]:
        return jsonify({
            "success": False,
            "message": "Invalid role."
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT user_id FROM users WHERE email=%s",
        (email,)
    )

    if cursor.fetchone():
        cursor.close()
        connection.close()
        return jsonify({
            "success": False,
            "message": "Email already registered."
        }), 409

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    cursor.execute("""
        INSERT INTO users
        (
            full_name,
            email,
            password_hash,
            role,
            department
        )
        VALUES
        (%s,%s,%s,%s,%s)
    """, (
        full_name,
        email,
        hashed_password,
        role,
        department
    ))

    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({
        "success": True,
        "message": "Account created successfully."
    }), 201


@auth.route("/login", methods=["POST"])
def login():

    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "success": False,
            "message": "Email and Password are required."
        }), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return jsonify({
            "success": False,
            "message": "Invalid Email or Password."
        }), 401

    if not bcrypt.check_password_hash(
        user["password_hash"],
        password
    ):
        return jsonify({
            "success": False,
            "message": "Invalid Email or Password."
        }), 401

    token = create_access_token(
        identity=str(user["user_id"]),
        additional_claims={
            "role": user["role"],
            "email": user["email"]
        }
    )

    return jsonify({
        "success": True,
        "message": "Login Successful",
        "token": token,
        "user": {
            "user_id": user["user_id"],
            "full_name": user["full_name"],
            "email": user["email"],
            "role": user["role"],
            "department": user["department"]
        }
    }), 200


@auth.route("/profile", methods=["GET"])
@jwt_required()
def profile():

    user_id = int(get_jwt_identity())

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            user_id,
            full_name,
            email,
            role,
            department,
            created_at
        FROM users
        WHERE user_id=%s
    """, (user_id,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({
        "success": True,
        "user": user
    }), 200


@auth.route("/admin/dashboard", methods=["GET"])
@jwt_required()
def admin_dashboard():

    claims = get_jwt()

    if claims["role"] != "GOVERNMENT_ADMIN":
        return jsonify({
            "success": False,
            "message": "Access Denied. Government users only."
        }), 403

    return jsonify({
        "success": True,
        "message": "Welcome Government Admin!"
    }), 200

