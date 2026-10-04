import re


class ParagraphCleaner:

    MIN_WORDS = 20

    @staticmethod
    def normalize(text):

        # Remove extra spaces, tabs and newlines
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def clean(paragraphs):

        cleaned = []

        paragraph_number = 1

        for paragraph in paragraphs:

            text = ParagraphCleaner.normalize(
                paragraph["paragraph_text"]
            )

            # Skip empty paragraphs
            if not text:
                continue

            word_count = len(text.split())

            # Skip very small paragraphs
            if word_count < ParagraphCleaner.MIN_WORDS:
                continue

            cleaned.append({

                "article_id": paragraph["article_id"],

                "paragraph_number": paragraph_number,

                "paragraph_text": text,

                "word_count": word_count,

                "status": paragraph["status"]

            })

            paragraph_number += 1

        return cleaned