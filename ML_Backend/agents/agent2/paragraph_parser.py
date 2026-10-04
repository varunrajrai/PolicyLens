class ParagraphParser:

    @staticmethod
    def split(article):

        article_id = article["article_id"]

        article_text = article["article_text"]

        raw_paragraphs = article_text.split("\n\n")

        paragraphs = []

        paragraph_number = 1

        for paragraph in raw_paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            paragraphs.append({

                "article_id": article_id,

                "paragraph_number": paragraph_number,

                "paragraph_text": paragraph,

                "word_count": len(paragraph.split()),

                "status": "PENDING"

            })

            paragraph_number += 1

        return paragraphs