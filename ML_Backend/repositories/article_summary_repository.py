from database.db import get_connection


class ArticleSummaryRepository:

    @staticmethod
    def bulk_insert(results):

        connection = get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO article_summary
        (
            article_id,
            summary,
            summary_model
        )
        VALUES
        (%s,%s,%s)
        """

        values = []

        for row in results:

            values.append(

                (

                    row["article_id"],
                    row["summary"],
                    row["summary_model"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} summaries.")

        cursor.close()
        connection.close()