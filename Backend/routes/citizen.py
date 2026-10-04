from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.citizen_service import CitizenService

citizen_bp = Blueprint("citizen", __name__)


# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------
@citizen_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():

    user_id = int(get_jwt_identity())

    dashboard = CitizenService.get_dashboard(user_id)

    return jsonify(dashboard), 200


# ---------------------------------------------------
# SUBMIT ARTICLE
# ---------------------------------------------------
@citizen_bp.route("/articles", methods=["POST"])
@jwt_required()
def submit_article():

    user_id = int(get_jwt_identity())

    data = request.get_json()

    response = CitizenService.submit_article(
        user_id,
        data
    )

    if not response["success"]:

        return jsonify(response), 400

    return jsonify(response), 201


# ---------------------------------------------------
# MY ARTICLES
# ---------------------------------------------------
@citizen_bp.route("/articles", methods=["GET"])
@jwt_required()
def get_articles():

    user_id = int(get_jwt_identity())

    articles = CitizenService.get_articles(user_id)

    return jsonify(articles), 200


@citizen_bp.route("/articles/<int:article_id>/review", methods=["GET"])
@jwt_required()
def get_policy_review(article_id):

    user_id = get_jwt_identity()

    result = CitizenService.get_policy_review(
        article_id,
        user_id
    )

    if not result["success"]:

        return jsonify({
            "message": result["message"]
        }), 404

    return jsonify(result), 200