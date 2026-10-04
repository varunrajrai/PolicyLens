from repositories.debate_repository import (
    DebateRepository
)

from agents.agent7.debate_generator import (
    DebateGenerator
)


class DebateAgent:

    @staticmethod
    def process():

        print("\n==============================")
        print("Agent 7 : Debate Generation")
        print("==============================\n")
        

        rows = DebateRepository.get_clause_paragraphs()

        grouped = {}

        # ---------------------------------------
        # Group by Clause
        # ---------------------------------------

        for row in rows:

            clause_id = row["clause_id"]

            if clause_id not in grouped:

                grouped[clause_id] = {

                    "clause_name": row["clause_name"],

                    "pro": [],

                    "anti": [],

                    "neutral": []

                }

            if row["stance"] == "Pro-CAA/NRC":

                grouped[clause_id]["pro"].append(

                    row["paragraph_text"]

                )

            elif row["stance"] == "Anti-CAA/NRC":

                grouped[clause_id]["anti"].append(

                    row["paragraph_text"]

                )

            else:

                grouped[clause_id]["neutral"].append(

                    row["paragraph_text"]

                )

        print(

            f"Found {len(grouped)} Clauses.\n"

        )

        generator = DebateGenerator()

        results = []

        # ---------------------------------------
        # Generate Debate
        # ---------------------------------------

        for clause_id, data in grouped.items():

            print("=" * 70)

            print(

                f"Generating Debate : "

                f"{data['clause_name']}"

            )

            print("=" * 70)

            debate = generator.generate_debate(

                clause_name=data["clause_name"],

                pro_paragraphs=data["pro"],

                anti_paragraphs=data["anti"],

                neutral_paragraphs=data["neutral"]

            )

            results.append(

                {

                    "clause_id":

                        clause_id,

                    "pro_argument":

                        debate["pro_argument"],

                    "anti_argument":

                        debate["anti_argument"],

                    "neutral_summary":

                        debate["neutral_summary"],

                    "consensus":

                        debate["consensus"],

                    "disagreement":

                        debate["disagreement"],

                    "model_name":

                        "gemini-3.5-flash"

                }

            )

            print("✔ Debate Generated\n")

        # ---------------------------------------
        # Save to Database
        # ---------------------------------------

        DebateRepository.bulk_insert(

            results

        )

        print("\n==============================")

        print("Agent 7 Completed")

        print("==============================\n")

        return results