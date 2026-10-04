from database.db import get_connection


class ArticleRepository:

    @staticmethod
    def create_article(article):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
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
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (

            article["user_id"],
            article["amendment_id"],
            article["title"],
            article["source"],
            article["source_url"],
            article["article_text"],
            article["uploaded_file"],
            article["language"],
            article["status"],
            article["current_stage"]

        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    @staticmethod
    def bulk_insert(articles):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
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
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = []

        for article in articles:

            values.append(

                (

                    article["user_id"],
                    article["amendment_id"],
                    article["title"],
                    article["source"],
                    article["source_url"],
                    article["article_text"],
                    article["uploaded_file"],
                    article["language"],
                    article["status"],
                    article["current_stage"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} articles successfully.")

        cursor.close()
        connection.close()

    @staticmethod
    def get_all_articles():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT

            article_id,

            title,

            article_text

        FROM articles

        ORDER BY article_id
        """

        cursor.execute(query)

        articles = cursor.fetchall()

        cursor.close()
        connection.close()

        return articles