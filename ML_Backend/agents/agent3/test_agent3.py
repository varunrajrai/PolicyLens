from agents.agent3.mapping_agent import MappingAgent

mappings = MappingAgent.process()

print()

for mapping in mappings[:10]:

    print("=" * 80)

    print(mapping)

    print()