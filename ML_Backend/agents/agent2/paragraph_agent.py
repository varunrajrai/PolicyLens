from repositories.article_repository import ArticleRepository
from repositories.paragraph_repository import ParagraphRepository

from agents.agent2.paragraph_parser import ParagraphParser
from agents.agent2.paragraph_cleaner import ParagraphCleaner


class ParagraphAgent:

    @staticmethod
    def process():

        print("\nFetching articles from database...\n")

        articles = ArticleRepository.get_all_articles()

        print(f"Articles Found : {len(articles)}")

        all_paragraphs = []

        for article in articles:

            print("\n" + "=" * 80)
            print(f"Article ID : {article['article_id']}")
            print(f"Title      : {article['title']}")
            print("=" * 80)

            # Step 1 : Split article into paragraphs
            paragraphs = ParagraphParser.split(article)

            print(f"Original Paragraphs : {len(paragraphs)}")

            # Step 2 : Clean paragraphs
            paragraphs = ParagraphCleaner.clean(paragraphs)

            print(f"Cleaned Paragraphs : {len(paragraphs)}")

            all_paragraphs.extend(paragraphs)

        print("\n" + "=" * 80)
        print(f"TOTAL PARAGRAPHS : {len(all_paragraphs)}")
        print("=" * 80)

        # Step 3 : Save into database
        ParagraphRepository.bulk_insert(all_paragraphs)

        print("\nAgent 2 completed successfully.")

        return all_paragraphs