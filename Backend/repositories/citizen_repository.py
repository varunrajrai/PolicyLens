from models.db import get_db_connection


class CitizenRepository:

    @staticmethod
    def get_user(user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                user_id,
                full_name,
                email,
                role
            FROM users
            WHERE user_id = %s
        """, (user_id,))

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user

    @staticmethod
    def get_dashboard_stats(user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Total Articles
        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM articles
            WHERE user_id = %s
        """, (user_id,))
        total_articles = cursor.fetchone()["total"]

        # Pending Articles
        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM articles
            WHERE user_id = %s
            AND status='PENDING'
        """, (user_id,))
        pending = cursor.fetchone()["total"]

        # Reviewed Articles
        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM articles
            WHERE user_id = %s
            AND status='REVIEWED'
        """, (user_id,))
        reviewed = cursor.fetchone()["total"]

        # Priority Selected Articles
        cursor.execute("""
    SELECT COUNT(DISTINCT p.article_id) AS total
    FROM paragraph_analysis pa
    INNER JOIN paragraphs p
        ON pa.paragraph_id = p.paragraph_id
    INNER JOIN articles a
        ON p.article_id = a.article_id
    WHERE a.user_id = %s
      AND pa.priority_score >= 3
""", (user_id,))
        priority_selected = cursor.fetchone()["total"]

        cursor.close()
        connection.close()

        return {
            "articles_submitted": total_articles,
            "under_review": pending,
            "priority_selected": priority_selected,
            "reviewed": reviewed
        }

    @staticmethod
    def get_recent_articles(user_id, limit=5):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                article_id,
                title,
                status,
                submission_date
            FROM articles
            WHERE user_id = %s
            ORDER BY submission_date DESC
            LIMIT %s
        """, (user_id, limit))

        articles = cursor.fetchall()

        cursor.close()
        connection.close()

        return articles
    
    @staticmethod
    def get_amendment_id(amendment_name):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT amendment_id
            FROM policy_amendments
            WHERE short_name = %s
        """, (amendment_name,))

        amendment = cursor.fetchone()

        cursor.close()
        connection.close()

        if amendment:
            return amendment["amendment_id"]

        return None


    @staticmethod
    def create_article(
        user_id,
        amendment_id,
        title,
        source,
        source_url,
        article_text
    ):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            INSERT INTO articles
            (
                user_id,
                amendment_id,
                title,
                source,
                source_url,
                article_text,
                uploaded_file,
                language,
                status,
                current_stage
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                NULL,
                'English',
                'PENDING',
                'INGESTED'
            )
        """, (
            user_id,
            amendment_id,
            title,
            source,
            source_url,
            article_text
        ))

        connection.commit()

        article_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return article_id


    @staticmethod
    def get_user_articles(user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                a.article_id,
                a.title,
                a.source,
                a.status,
                a.current_stage,
                a.submission_date,
                pa.short_name AS amendment
            FROM articles a
            INNER JOIN policy_amendments pa
                ON a.amendment_id = pa.amendment_id
            WHERE a.user_id = %s
            ORDER BY a.submission_date DESC
        """, (user_id,))

        articles = cursor.fetchall()

        cursor.close()
        connection.close()

        return articles
    
    @staticmethod
    def get_policy_review(article_id, user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True,buffered=True)

        # ---------------------------------------------------
        # Article Information
        # ---------------------------------------------------

        cursor.execute("""
            SELECT
                a.article_id,
                a.title,
                a.source,
                a.article_text,
                a.status,
                a.current_stage,
                a.submission_date,
                p.name AS amendment
            FROM articles a
            INNER JOIN policy_amendments p
                ON a.amendment_id = p.amendment_id
            WHERE
                a.article_id=%s
            AND
                a.user_id=%s
        """, (article_id, user_id))

        article = cursor.fetchone()

        if not article:

            cursor.close()
            connection.close()

            return None

        # ---------------------------------------------------
        # AI Summary
        # ---------------------------------------------------

        cursor.execute("""
            SELECT
                summary
            FROM article_summary
            WHERE article_id=%s
        """, (article_id,))

        summary = cursor.fetchone()

        # ---------------------------------------------------
        # Overall Stance
        # ---------------------------------------------------

        cursor.execute("""
            SELECT
                stance,
                COUNT(*) AS total
            FROM paragraph_stance ps
            INNER JOIN paragraphs p
                ON ps.paragraph_id=p.paragraph_id
            WHERE p.article_id=%s
            GROUP BY stance
            ORDER BY total DESC
        """, (article_id,))

        stance_rows = cursor.fetchall()

        overall_stance = "Unknown"

        if stance_rows:
            overall_stance = stance_rows[0]["stance"]

        stance_distribution = {}

        for row in stance_rows:

            stance_distribution[row["stance"]] = row["total"]

        # ---------------------------------------------------
        # Paragraph Statistics
        # ---------------------------------------------------

        cursor.execute("""
            SELECT

                COUNT(*) AS paragraphs,

                AVG(pa.priority_score) AS average_priority,

                SUM(
                    CASE
                        WHEN pa.priority_score>=3
                        THEN 1
                        ELSE 0
                    END
                ) AS high_priority_count

            FROM paragraph_analysis pa

            INNER JOIN paragraphs p

            ON pa.paragraph_id=p.paragraph_id

            WHERE p.article_id=%s

        """, (article_id,))

        stats = cursor.fetchone()

        # ---------------------------------------------------
        # Average Confidence
        # ---------------------------------------------------

        cursor.execute("""
            SELECT

                ROUND(
                    AVG(confidence),
                    2
                ) AS average_confidence

            FROM paragraph_stance ps

            INNER JOIN paragraphs p

            ON ps.paragraph_id=p.paragraph_id

            WHERE p.article_id=%s

        """, (article_id,))

        confidence = cursor.fetchone()

        # ---------------------------------------------------
        # Clause Statistics
        # ---------------------------------------------------

        cursor.execute("""
            SELECT

                cm.clause_name,

                COUNT(*) AS paragraph_count,

                ROUND(
                    AVG(main_similarity)*100,
                    2
                ) AS average_similarity

            FROM paragraph_clause_mapping pcm

            INNER JOIN clause_master cm

            ON pcm.main_clause_id=cm.clause_id

            INNER JOIN paragraphs p

            ON pcm.paragraph_id=p.paragraph_id

            WHERE p.article_id=%s

            GROUP BY cm.clause_id

            ORDER BY paragraph_count DESC

        """, (article_id,))

        clauses = cursor.fetchall()

        cursor.close()
        connection.close()

        return {

        "article": article,

        "summary": (
            summary["summary"]
            if summary
            else "No AI-generated summary is currently available for this article."
        ),

        "statistics": {

            "overall_stance": (
                overall_stance
                if overall_stance != "Unknown"
                else "Not Available"
            ),

            "paragraphs": (
                stats["paragraphs"]
                if stats["paragraphs"] is not None
                else 0
            ),

            "high_priority": (
                stats["high_priority_count"]
                if stats["high_priority_count"] is not None
                else 0
            ),

            "average_priority": (
                round(float(stats["average_priority"]), 2)
                if stats["average_priority"] is not None
                else 0
            ),

            "average_confidence": (
                round(float(confidence["average_confidence"]) * 100, 2)
                if confidence["average_confidence"] is not None
                else 0
            ),

            "detected_clauses": len(clauses)

        },

        "stance_distribution": {

            "Pro-CAA/NRC":
                stance_distribution.get("Pro-CAA/NRC", 0),

            "Anti-CAA/NRC":
                stance_distribution.get("Anti-CAA/NRC", 0),

            "Neutral":
                stance_distribution.get("Neutral", 0)

        },

        "clauses": clauses if clauses else [],

        "analysis_status": {

            "summary_available": summary is not None,

            "stance_available": len(stance_rows) > 0,

            "priority_available": (
                stats["paragraphs"] is not None
                and stats["paragraphs"] > 0
            ),

            "clauses_available": len(clauses) > 0

        }

    }