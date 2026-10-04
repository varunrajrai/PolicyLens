from database.db import get_connection


class DebateRepository:

    @staticmethod
    def get_clause_paragraphs():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """

        SELECT

            cm.clause_id,

            cm.clause_name,

            ps.stance,

            p.paragraph_text,

            a.title,

            a.source,

            ps.confidence

        FROM paragraph_stance ps

        JOIN paragraphs p

            ON ps.paragraph_id = p.paragraph_id

        JOIN clause_master cm

            ON ps.main_clause_id = cm.clause_id

        JOIN articles a

            ON p.article_id = a.article_id

        ORDER BY

            cm.clause_id,

            ps.stance,

            ps.confidence DESC;

        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows

    @staticmethod
    def bulk_insert(results):

        connection = get_connection()

        cursor = connection.cursor()

        query = """

        INSERT INTO clause_debates
        (

            clause_id,

            pro_argument,

            anti_argument,

            neutral_summary,

            consensus,

            disagreement,

            model_name

        )

        VALUES

        (

            %s,%s,%s,%s,%s,%s,%s

        )

        """

        values = []

        for row in results:

            values.append(

                (

                    row["clause_id"],

                    row["pro_argument"],

                    row["anti_argument"],

                    row["neutral_summary"],

                    row["consensus"],

                    row["disagreement"],

                    row["model_name"]

                )

            )

        cursor.executemany(

            query,

            values

        )

        connection.commit()

        print(

            f"\nInserted {cursor.rowcount} debates."

        )

        cursor.close()

        connection.close()