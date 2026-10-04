from repositories.paragraph_repository import ParagraphRepository
from repositories.paragraph_mapping_repository import ParagraphMappingRepository
from repositories.paragraph_analysis_repository import ParagraphAnalysisRepository

from agents.agent4.priority_engine import PriorityEngine


class PriorityAgent:

    @staticmethod
    def process():

        paragraphs = ParagraphRepository.get_all_paragraphs()

        mappings = ParagraphMappingRepository.get_all_mappings()

        mapping_lookup = {}

        clause_counts = {}

        for mapping in mappings:

            mapping_lookup[mapping["paragraph_id"]] = mapping

            clause = mapping["main_clause_name"]

            clause_counts[clause] = clause_counts.get(clause, 0) + 1

        total = len(paragraphs)

        results = []

        for paragraph in paragraphs:

            mapping = mapping_lookup.get(paragraph["paragraph_id"])

            if mapping is None:

                continue

            score, citation_count = PriorityEngine.score(

                paragraph["paragraph_text"],

                mapping["main_clause_name"],

                clause_counts,

                total

            )

            if score == -1:

                continue

            results.append({

                "paragraph_id": paragraph["paragraph_id"],

                "priority_score": score,

                "citation_count": citation_count

            })

        ParagraphAnalysisRepository.bulk_insert(results)

        print("\nAgent 4 Completed.")

        return results