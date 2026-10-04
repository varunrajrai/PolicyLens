import os
import json
import time

from google import genai


class DebateGenerator:

    def __init__(self):

        print("\nLoading Gemini Debate Generator...\n")


        self.client = genai.Client(

            api_key=os.getenv("GEMINI_API_KEY_1")

        )

        self.model = "gemini-3.5-flash"


    def generate_debate(

        self,

        clause_name,

        pro_paragraphs,

        anti_paragraphs,

        neutral_paragraphs

    ):

        pro_text = "\n\n".join(pro_paragraphs)

        anti_text = "\n\n".join(anti_paragraphs)

        neutral_text = "\n\n".join(neutral_paragraphs)

        prompt = f"""
You are an expert constitutional scholar and public policy analyst.

Your task is to generate a balanced debate for the following policy clause.

Clause:
{clause_name}

--------------------------------------------------

PRO ARGUMENTS

{pro_text}

--------------------------------------------------

ANTI ARGUMENTS

{anti_text}

--------------------------------------------------

NEUTRAL / FACTUAL PARAGRAPHS

{neutral_text}

--------------------------------------------------

Generate the following:

1. pro_argument
Summarize the strongest arguments supporting this clause.

2. anti_argument
Summarize the strongest arguments opposing this clause.

3. neutral_summary
Summarize only the factual and legal information.

4. consensus
Mention facts on which both sides indirectly agree.

5. disagreement
Mention the biggest disagreement.

Rules

• Do NOT invent facts.

• Only use information present above.

• Write each section in approximately 150-250 words.

• Maintain an objective tone.

Return ONLY valid JSON.

{{
    "pro_argument":"",
    "anti_argument":"",
    "neutral_summary":"",
    "consensus":"",
    "disagreement":""
}}
"""

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt

        )

        text = response.text.strip()

        text = (

            text

            .replace("```json", "")

            .replace("```", "")

            .strip()

        )

        start = text.find("{")

        end = text.rfind("}") + 1

        debate = json.loads(

            text[start:end]

        )

        return debate