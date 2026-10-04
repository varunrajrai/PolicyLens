from database.db import get_connection


class ClauseRepository:

    @staticmethod
    def get_all_clauses():

        connection = get_connection()

        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT

            clause_id,

            clause_name,

            clause_description

        FROM clause_master

        ORDER BY clause_order
        """

        cursor.execute(query)

        clauses = cursor.fetchall()

        cursor.close()
        connection.close()

        return clauses