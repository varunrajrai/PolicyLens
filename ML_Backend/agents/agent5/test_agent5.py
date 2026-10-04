from agents.agent5.summary_agent import SummaryAgent


results = SummaryAgent.process()

print()

for row in results:

    print("=" * 80)

    print(

        f"Article : {row['article_id']}"

    )

    print()

    print(row["summary"])

    print()