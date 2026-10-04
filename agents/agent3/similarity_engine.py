from sentence_transformers import util


class SimilarityEngine:

    @staticmethod
    def calculate(paragraph_embedding, clause_embeddings):

        similarities = util.cos_sim(
            paragraph_embedding,
            clause_embeddings
        )[0]

        return similarities