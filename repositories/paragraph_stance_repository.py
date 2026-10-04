from database.db import get_connection

from dotenv import load_dotenv
load_dotenv()
class ParagraphStanceRepository:

    @staticmethod
    def bulk_insert(results):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO paragraph_stance
        (

            paragraph_id,

            main_clause_id,

            stance,

            confidence,

            score_pro,

            score_anti,

            score_neutral,

            model_name

        )

        VALUES

        (%s,%s,%s,%s,%s,%s,%s,%s)

        """

        values = []

        for row in results:

            values.append(

                (

                    row["paragraph_id"],

                    row["main_clause_id"],

                    row["stance"],

                    row["confidence"],

                    row["score_pro"],

                    row["score_anti"],

                    row["score_neutral"],

                    row["model_name"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} stance rows.")

        cursor.close()

        connection.close()