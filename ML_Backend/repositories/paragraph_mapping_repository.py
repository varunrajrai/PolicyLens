from database.db import get_connection


class ParagraphMappingRepository:

    @staticmethod
    def bulk_insert(mappings):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO paragraph_clause_mapping
        (
            paragraph_id,
            main_clause_id,
            sub_clause_id,
            main_similarity,
            sub_similarity,
            model_name
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """

        values = []

        for mapping in mappings:

            values.append(

                (

                    mapping["paragraph_id"],
                    mapping["main_clause_id"],
                    mapping["sub_clause_id"],
                    mapping["main_similarity"],
                    mapping["sub_similarity"],
                    mapping["model_name"]

                )

            )

        cursor.executemany(query, values)

        connection.commit()

        print(f"\nInserted {cursor.rowcount} mappings.")

        cursor.close()
        connection.close()

    @staticmethod
    def get_all_mappings():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT

            pcm.paragraph_id,

            pcm.main_clause_id,

            cm.clause_name AS main_clause_name

        FROM paragraph_clause_mapping pcm

        JOIN clause_master cm
        ON pcm.main_clause_id = cm.clause_id

        ORDER BY pcm.paragraph_id
        """

        cursor.execute(query)

        mappings = cursor.fetchall()

        cursor.close()
        connection.close()

        return mappings