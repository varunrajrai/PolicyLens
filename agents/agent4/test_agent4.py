from agents.agent4.priority_agent import PriorityAgent

results = PriorityAgent.process()

print()

for row in results[:20]:

    print("=" * 80)

    print(row)