import re


class PriorityEngine:

    legal_keywords = [

        'constitution',
        'article',
        'unconstitutional',
        'implement',
        'violates',
        'section',
        'clause',
        'legal',
        'court',
        'petition',
        'statute',
        'fundamental',
        'rights',
        'amendment',
        'parliament',
        'legislation',
        'provision',
        'validity',
        'ultra',
        'vires',
        'subordinate',
        'legislature',
        'enforce'

    ]

    feasibility_words = [

        'implement',
        'infrastructure',
        'enforce',
        'process',
        'cannot',
        'difficult',
        'challenge',
        'concern',
        'risk',
        'comply',
        'compliance',
        'refuse',
        'repeal',
        'validity',
        'invalid',
        'infirmity',
        'infirmities'

    ]

    citation_pattern = re.compile(

        r'(article\s+\d+|section\s+\d+|clause\s+[\(\d]|sub.?rule|sub.?section'
        r'|citizenship act|amendment act \d{4}|constitution of india'
        r'|supreme court|high court)',

        re.IGNORECASE

    )

    noise_pattern = re.compile(

        r'this article went live|discover\.\.\.|police station|woman who accused',

        re.IGNORECASE

    )

    @staticmethod
    def score(paragraph, clause_name, clause_counts, total):

        score = 0

        words = paragraph.split()

        word_count = len(words)

        lower = paragraph.lower()

        if PriorityEngine.noise_pattern.search(paragraph) or word_count < 20:

            return -1, 0

        legal_hits = sum(

            1

            for word in words

            if word.lower().strip(".()") in PriorityEngine.legal_keywords

        )

        citations = PriorityEngine.citation_pattern.findall(paragraph)

        citation_count = len(citations)

        if legal_hits >= 2:

            score += 1

        if citation_count >= 2:

            score += 1

        if word_count > 60:

            score += 1

        if any(

            word in lower

            for word in PriorityEngine.feasibility_words

        ):

            score += 1

        if clause_counts.get(clause_name, 0) / total < 0.15:

            score += 1

        if citation_count >= 3:

            score = max(score, 3)

        return score, citation_count