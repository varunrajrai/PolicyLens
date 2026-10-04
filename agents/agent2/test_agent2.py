from agents.agent2.paragraph_agent import ParagraphAgent

paragraphs = ParagraphAgent.process()

print("\n")

for paragraph in paragraphs[:10]:

    print("=" * 80)

    print("Article ID :", paragraph["article_id"])

    print("Paragraph Number :", paragraph["paragraph_number"])

    print("Word Count :", paragraph["word_count"])

    print()

    print(paragraph["paragraph_text"][:300])

    print()