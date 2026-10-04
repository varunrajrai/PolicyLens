from agents.agent6.stance_agent import StanceAgent


results = StanceAgent.process()

for row in results[:10]:

    print("=" * 80)

    print(row)

    print()