from pathlib import Path

from agents.agent1.docx_parser import DocxParser
from agents.agent1.cleaner import TextCleaner
from agents.agent1.splitter import ArticleSplitter

from utils.datasets import DATASETS

from repositories.article_repository import ArticleRepository


class IngestionAgent:

    # Map each source to its corresponding user_id
    SOURCE_USER_MAP = {
        "The Wire": 1,
        "OpIndia": 2,
        "General Articles": 3
    }

    AMENDMENT_ID = 1

    @staticmethod
    def ingest():

        base_dir = Path(__file__).resolve().parents[2]

        all_articles = []

        for dataset in DATASETS:

            print("\n" + "=" * 80)
            print(f"Processing : {dataset['source']}")
            print("=" * 80)

            file_path = base_dir / "uploads" / dataset["file"]

            if not file_path.exists():
                print(f"File not found : {file_path}")
                continue

            # Step 1: Parse
            paragraphs = DocxParser.extract_paragraphs(str(file_path))
            print(f"Original Paragraphs : {len(paragraphs)}")

            # Step 2: Clean
            paragraphs = TextCleaner.clean(paragraphs)
            print(f"Cleaned Paragraphs : {len(paragraphs)}")

            # Step 3: Split
            articles = ArticleSplitter.split_articles(
                paragraphs,
                dataset["titles"]
            )

            print(f"Articles Found : {len(articles)}")

            # Step 4: Build Article Objects
            for article in articles:

                all_articles.append({

                    "user_id": IngestionAgent.SOURCE_USER_MAP[dataset["source"]],

                    "amendment_id": IngestionAgent.AMENDMENT_ID,

                    "title": article["title"],

                    "source": dataset["source"],

                    "source_url": None,

                    "article_text": article["article_text"],

                    "uploaded_file": dataset["file"],

                    "language": "English",

                    "status": "PENDING",

                    "current_stage": "INGESTED"

                })

        print("\n" + "=" * 80)
        print(f"TOTAL ARTICLES : {len(all_articles)}")
        print("=" * 80)

        ArticleRepository.bulk_insert(all_articles)

        return all_articles