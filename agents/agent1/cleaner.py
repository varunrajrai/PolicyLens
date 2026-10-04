import re


class TextCleaner:

    # Paragraphs matching these patterns will be removed
    NOISE_PATTERNS = [

        re.compile(r'^\s*$', re.IGNORECASE),

        re.compile(r'^\s*Advertisement\s*$', re.IGNORECASE),

        re.compile(r'^\s*Article\s+\d+\s*$', re.IGNORECASE),

        re.compile(r'this article (went live|is (from|part))',
                   re.IGNORECASE),

        re.compile(r'^\s*(Photo|Image|Illustration)\s*:',
                   re.IGNORECASE),

        re.compile(r'^Representative Image',
                   re.IGNORECASE),

        re.compile(r'^Representative Photo',
                   re.IGNORECASE),

        re.compile(r'^File Photo',
                   re.IGNORECASE),

        re.compile(r'^Photo Courtesy',
                   re.IGNORECASE),

        re.compile(r'^Image Courtesy',
                   re.IGNORECASE),

        re.compile(r'^Read More',
                   re.IGNORECASE),

        re.compile(r'^Follow Us',
                   re.IGNORECASE),

        re.compile(r'^Continue Reading',
                   re.IGNORECASE),

        re.compile(r'^Share',
                   re.IGNORECASE),

        re.compile(r'^Subscribe',
                   re.IGNORECASE),

        re.compile(r'^Get Instant Alerts',
                   re.IGNORECASE),
    ]

    @staticmethod
    def normalize(text: str) -> str:
        """
        Removes extra spaces, tabs and newlines.
        """

        return " ".join(text.split())

    @staticmethod
    def is_noise(text: str) -> bool:

        text = TextCleaner.normalize(text)

        for pattern in TextCleaner.NOISE_PATTERNS:

            if pattern.search(text):
                return True

        return False

    @staticmethod
    def clean(paragraphs):

        cleaned = []

        removed = 0

        for paragraph in paragraphs:

            paragraph = TextCleaner.normalize(paragraph)

            if TextCleaner.is_noise(paragraph):
                removed += 1
                continue

            cleaned.append(paragraph)

        print(f"Removed {removed} noisy paragraphs.")

        return cleaned