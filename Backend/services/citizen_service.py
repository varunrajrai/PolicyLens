from repositories.citizen_repository import CitizenRepository


class CitizenService:

    @staticmethod
    def get_dashboard(user_id):

        user = CitizenRepository.get_user(user_id)

        stats = CitizenRepository.get_dashboard_stats(user_id)

        recent_articles = CitizenRepository.get_recent_articles(user_id)

        return {

            "user_name": user["full_name"],

            **stats,

            "recent_articles": recent_articles

        }
    
    from repositories.citizen_repository import CitizenRepository


class CitizenService:

    # -----------------------------
    # Existing Dashboard Methods
    # -----------------------------

    @staticmethod
    def get_dashboard(user_id):

        user = CitizenRepository.get_user(user_id)

        stats = CitizenRepository.get_dashboard_stats(user_id)

        recent_articles = CitizenRepository.get_recent_articles(user_id)

        return {
            "user_name": user["full_name"],
            "articles_submitted": stats["articles_submitted"],
            "under_review": stats["under_review"],
            "priority_selected": stats["priority_selected"],
            "used_in_reports": stats["reviewed"],
            "recent_articles": recent_articles
        }

    # -----------------------------
    # Submit Article
    # -----------------------------

    @staticmethod
    def submit_article(user_id, data):

        amendment_name = data.get("amendment")

        amendment_id = CitizenRepository.get_amendment_id(
            amendment_name
        )

        if amendment_id is None:

            return {
                "success": False,
                "message": "Invalid amendment selected."
            }

        article_id = CitizenRepository.create_article(
            user_id=user_id,
            amendment_id=amendment_id,
            title=data.get("title"),
            source=data.get("source"),
            source_url=data.get("url"),
            article_text=data.get("article")
        )

        return {
            "success": True,
            "message": "Article submitted successfully.",
            "article_id": article_id
        }

    # -----------------------------
    # My Articles
    # -----------------------------

    @staticmethod
    def get_articles(user_id):

        articles = CitizenRepository.get_user_articles(
            user_id
        )

        return articles
    
    @staticmethod
    def get_policy_review(article_id, user_id):

        review = CitizenRepository.get_policy_review(
            article_id,
            user_id
        )

        if review is None:

            return {
                "success": False,
                "message": "Article not found."
            }

        return {
            "success": True,
            "data": review
        }