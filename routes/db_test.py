from flask import Blueprint, jsonify

from database.db import get_connection

db_bp = Blueprint("database", __name__)


@db_bp.route("/test-db", methods=["GET"])
def test_database():

    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("SELECT DATABASE();")

        database = cursor.fetchone()[0]

        return jsonify({
            "status": "success",
            "database": database
        }), 200

    except Exception as e:

        return jsonify({
            "status": "failed",
            "error": str(e)
        }), 500

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()