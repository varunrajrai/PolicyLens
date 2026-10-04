from repositories.paragraph_analysis_repository import (
    ParagraphAnalysisRepository
)

from repositories.paragraph_stance_repository import (
    ParagraphStanceRepository
)

from agents.agent6.stance_classifier import (
    StanceClassifier
)


class StanceAgent:

    @staticmethod
    def process():

        print("\n==============================")
        print("Agent 6 : Stance Detection")
        print("==============================\n")

        paragraphs = (
            ParagraphAnalysisRepository
            .get_priority_paragraphs()
        )

        classifier = StanceClassifier()

        batch_size = 8

        total = len(paragraphs)

        results = []

        for start in range(0, total, batch_size):

            batch = paragraphs[start:start + batch_size]

            paragraph_texts = [

                row["paragraph_text"]

                for row in batch

            ]

            clauses = [

                row["clause_name"]

                for row in batch

            ]

            predictions = classifier.classify_batch(

                paragraph_texts,

                clauses

            )

            for row, prediction in zip(

                batch,

                predictions

            ):

                results.append(

                    {

                        "paragraph_id":

                        row["paragraph_id"],

                        "main_clause_id":

                        row["main_clause_id"],

                        "stance":

                        prediction["stance"],

                        "confidence":

                        prediction["confidence"],

                        "score_pro":

                        prediction["score_pro"],

                        "score_anti":

                        prediction["score_anti"],

                        "score_neutral":

                        prediction["score_neutral"],

                        "model_name":

                        "Political_DEBATE_large_v1.0"

                    }

                )

            end = min(

                start + batch_size,

                total

            )

            print(

                f"✔ {end}/{total} paragraphs processed"

            )

        ParagraphStanceRepository.bulk_insert(

            results

        )

        print("\n==============================")
        print("Agent 6 Completed")
        print("==============================\n")

        return results