import torch

from agents.agent3.clause_embedder import ClauseEmbedder
from agents.agent3.similarity_engine import SimilarityEngine


class ClauseMapper:

    def __init__(self):

        self.embedder = ClauseEmbedder()

    def map_paragraph(self, paragraph, clauses):

        clause_embeddings = self.embedder.encode_clauses(clauses)

        paragraph_embedding = self.embedder.encode_paragraph(
            paragraph["paragraph_text"]
        )

        similarities = SimilarityEngine.calculate(
            paragraph_embedding,
            clause_embeddings
        )

        top_two = torch.topk(similarities, k=2)

        first = top_two.indices[0].item()
        second = top_two.indices[1].item()

        return {

            "paragraph_id": paragraph["paragraph_id"],

            "main_clause_id": clauses[first]["clause_id"],

            "sub_clause_id": clauses[second]["clause_id"],

            "main_similarity": float(
                top_two.values[0]
            ),

            "sub_similarity": float(
                top_two.values[1]
            ),

            "model_name": "all-MiniLM-L6-v2"

        }