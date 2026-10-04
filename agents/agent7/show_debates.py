from database.db import get_connection


def show_debates():

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT

        cd.debate_id,

        cm.clause_name,

        cd.pro_argument,

        cd.anti_argument,

        cd.neutral_summary,

        cd.consensus,

        cd.disagreement

    FROM clause_debates cd

    JOIN clause_master cm

        ON cd.clause_id = cm.clause_id

    ORDER BY cm.clause_id;
    """

    cursor.execute(query)

    debates = cursor.fetchall()

    cursor.close()
    connection.close()

    print("\n" + "=" * 120)
    print("POLICYLENS - CLAUSE DEBATES")
    print("=" * 120)

    for debate in debates:

        print("\n" + "=" * 120)
        print(f"Clause : {debate['clause_name']}")
        print("=" * 120)

        print("\n🟢 PRO ARGUMENT\n")
        print(debate["pro_argument"])

        print("\n🔴 ANTI ARGUMENT\n")
        print(debate["anti_argument"])

        print("\n⚪ NEUTRAL SUMMARY\n")
        print(debate["neutral_summary"])

        print("\n🤝 CONSENSUS\n")
        print(debate["consensus"])

        print("\n⚔️ MAIN DISAGREEMENT\n")
        print(debate["disagreement"])

        print("\n" + "-" * 120)


if __name__ == "__main__":
    show_debates()