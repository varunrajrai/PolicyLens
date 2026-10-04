class ArticleSplitter:

    @staticmethod
    def split_articles(paragraphs, titles):

        articles = []

        current_article = None

        # Faster lookup
        title_set = set(titles)

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            # New article starts
            if paragraph in title_set:

                # Save previous article
                if current_article:

                    current_article["article_text"] = "\n\n".join(
                        current_article["article_text"]
                    )

                    articles.append(current_article)

                current_article = {
                    "title": paragraph,
                    "article_text": []
                }

            else:

                if current_article:
                    current_article["article_text"].append(paragraph)

        # Save last article
        if current_article:

            current_article["article_text"] = "\n\n".join(
                current_article["article_text"]
            )

            articles.append(current_article)

        return articles