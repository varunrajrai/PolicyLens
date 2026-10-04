from database.db import get_connection


class ParagraphAnalysisRepository:

    @staticmethod
    def bulk_insert(results):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO paragraph_analysis
        (
            paragraph_id,
            priority_score,
            citation_count
        )
        VALUES
        (%s,%s,%s)
        """

        values = []

        for row in results:

            values.append(

                (

                    row["paragraph_id"],
                    row["priority_score"],
                    row["citation_count"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} paragraph analysis rows.")

        cursor.close()
        connection.close()

    @staticmethod
    def get_priority_paragraphs():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """

        SELECT

            p.paragraph_id,

            p.paragraph_text,

            pcm.main_clause_id,

            cm.clause_name,

            pa.priority_score

        FROM paragraphs p

        JOIN paragraph_clause_mapping pcm

            ON p.paragraph_id = pcm.paragraph_id

        JOIN clause_master cm

            ON pcm.main_clause_id = cm.clause_id

        JOIN paragraph_analysis pa

            ON p.paragraph_id = pa.paragraph_id

        WHERE pa.priority_score >= 3

        ORDER BY p.paragraph_id

        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()

        connection.close()

        return rows