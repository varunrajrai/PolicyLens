from repositories.paragraph_repository import ParagraphRepository
from repositories.clause_repository import ClauseRepository
from repositories.paragraph_mapping_repository import ParagraphMappingRepository

from agents.agent3.clause_mapper import ClauseMapper


class MappingAgent:

    @staticmethod
    def process():

        print("\nLoading paragraphs...")

        paragraphs = ParagraphRepository.get_all_paragraphs()

        print(f"Paragraphs : {len(paragraphs)}")

        print("\nLoading clauses...")

        clauses = ClauseRepository.get_all_clauses()

        print(f"Clauses : {len(clauses)}")

        mapper = ClauseMapper()

        mappings = []

        for paragraph in paragraphs:

            mapping = mapper.map_paragraph(
                paragraph,
                clauses
            )

            mappings.append(mapping)

        ParagraphMappingRepository.bulk_insert(
            mappings
        )

        print("\nAgent 3 Completed.")

        return mappings