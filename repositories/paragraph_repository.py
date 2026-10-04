from database.db import get_connection


class ParagraphRepository:

    @staticmethod
    def bulk_insert(paragraphs):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO paragraphs
        (
            article_id,
            paragraph_number,
            paragraph_text,
            word_count,
            status
        )
        VALUES
        (%s,%s,%s,%s,%s)
        """

        values = []

        for paragraph in paragraphs:

            values.append(

                (

                    paragraph["article_id"],

                    paragraph["paragraph_number"],

                    paragraph["paragraph_text"],

                    paragraph["word_count"],

                    paragraph["status"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} paragraphs successfully.")

        cursor.close()
        connection.close()


    @staticmethod
    def get_paragraphs_by_article(article_id):

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
            paragraph_id,
            article_id,
            paragraph_number,
            paragraph_text,
            word_count,
            status
        FROM paragraphs
        WHERE article_id = %s
        ORDER BY paragraph_number
        """

        cursor.execute(query, (article_id,))

        paragraphs = cursor.fetchall()

        cursor.close()
        connection.close()

    @staticmethod
    def get_all_paragraphs():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT

            paragraph_id,

            article_id,

            paragraph_number,

            paragraph_text

        FROM paragraphs

        ORDER BY article_id,
                 paragraph_number
        """

        cursor.execute(query)

        paragraphs = cursor.fetchall()

        cursor.close()
        connection.close()

        return paragraphs

        return paragraphs