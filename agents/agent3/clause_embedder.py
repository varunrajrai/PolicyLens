from sentence_transformers import SentenceTransformer


class ClauseEmbedder:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def encode_clauses(self, clauses):

        clause_texts = []

        for clause in clauses:

            clause_texts.append(clause["clause_description"])

        embeddings = self.model.encode(
            clause_texts,
            convert_to_tensor=True
        )

        return embeddings

    def encode_paragraph(self, paragraph):

        return self.model.encode(
            paragraph,
            convert_to_tensor=True
        )