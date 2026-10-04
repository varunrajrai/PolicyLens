from repositories.article_repository import ArticleRepository

from repositories.article_summary_repository import (
    ArticleSummaryRepository
)

from agents.agent5.summarizer import summarize_article


class SummaryAgent:

    @staticmethod
    def process():

        articles = ArticleRepository.get_all_articles()

        summaries = []

        for article in articles:

            print("\n" + "=" * 80)

            print(

                f"Processing : {article['title']}"

            )

            summary = summarize_article(

                article["article_text"]

            )

            summaries.append(

                {

                    "article_id":

                    article["article_id"],

                    "summary":

                    summary,

                    "summary_model":

                    "facebook/bart-large-cnn"

                }

            )

        ArticleSummaryRepository.bulk_insert(

            summaries

        )

        print(

            "\nAgent 5 Completed."

        )

        return summaries