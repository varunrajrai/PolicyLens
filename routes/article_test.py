from flask import Blueprint, jsonify

from repositories.article_repository import ArticleRepository

article_bp = Blueprint("articles", __name__)


@article_bp.route("/articles", methods=["GET"])
def get_articles():

    articles = ArticleRepository.get_all_articles()

    return jsonify({
        "count": len(articles),
        "articles": articles
    })