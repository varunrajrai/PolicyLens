import os
import json
import time

from google import genai


class StanceClassifier:

    def __init__(self):

        print("\nLoading Gemini API...\n")

        self.api_keys = [

            os.getenv("GEMINI_API_KEY_1"),
            os.getenv("GEMINI_API_KEY_2"),
            os.getenv("GEMINI_API_KEY_3"),
            os.getenv("GEMINI_API_KEY_4")

        ]

        self.api_keys = [

            key

            for key in self.api_keys

            if key is not None and key.strip() != ""

        ]

        if len(self.api_keys) == 0:

            raise Exception("No Gemini API Keys Found!")

        self.clients = [

            genai.Client(api_key=key)

            for key in self.api_keys

        ]

        self.current_client = 0

        self.model = "gemini-3.5-flash"

        print(f"{len(self.clients)} API Keys Loaded Successfully.\n")

    def classify_batch(self, paragraphs, clauses):

        results = []

        total = len(paragraphs)

        for index, (paragraph, clause) in enumerate(

            zip(paragraphs, clauses),

            start=1

        ):

            while True:

                prompt = f"""
You are an expert policy analyst.

Classify the paragraph into EXACTLY one label.

Labels:

- Pro-CAA/NRC
- Anti-CAA/NRC
- Neutral

Definitions:

• Pro-CAA/NRC:
Supports or defends the Citizenship Amendment Act,
its implementation,
government policy,
or arguments favouring it.

• Anti-CAA/NRC:
Criticises,
opposes,
or highlights negative consequences,
constitutional concerns,
human rights concerns,
or discrimination relating to CAA/NRC.

• Neutral:
Purely factual reporting without supporting or opposing the Act.


Clause:
{clause}

Paragraph:
{paragraph}

Return ONLY valid JSON.

{{
"stance":"Pro-CAA/NRC",
"confidence":0.95,
"score_pro":0.95,
"score_anti":0.03,
"score_neutral":0.02
}}
"""

                client = self.clients[self.current_client]

                print("\n" + "=" * 80)
                print(
                    f"Paragraph {index}/{total}"
                )
                print(
                    f"Using API Key {self.current_client + 1}"
                )
                print("=" * 80)

                try:

                    response = client.models.generate_content(

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

                    prediction = json.loads(text)

                    results.append(prediction)

                    print("\nPrediction")

                    print(

                        json.dumps(

                            prediction,

                            indent=4

                        )

                    )

                    print(

                        f"\nCompleted {index}/{total}"

                    )

                    break

                except Exception as e:

                    print("\nERROR")

                    print(e)

                    # Quota exhausted
                    if "429" in str(e):

                        print(

                            "\nQuota exhausted."

                        )

                        self.current_client += 1

                        if self.current_client >= len(self.clients):

                            print(

                                "\nAll API Keys exhausted."

                            )

                            print(

                                "Waiting 60 seconds..."

                            )

                            self.current_client = 0

                            time.sleep(60)

                        else:

                            print(

                                f"Switching to API Key "

                                f"{self.current_client + 1}"

                            )

                        continue

                    # Server error (Gemini API side issue)
                    if (

                        "500" in str(e)

                        or "502" in str(e)

                        or "503" in str(e)

                        or "504" in str(e)

                        or "server error" in str(e).lower()

                        or "internal error" in str(e).lower()

                    ):

                        print(

                            "\nServer error."

                        )

                        print(

                            "Retrying in 15 seconds..."

                        )

                        time.sleep(15)

                        continue

                    prediction = {

                        "stance": "Neutral",

                        "confidence": 0.50,

                        "score_pro": 0.33,

                        "score_anti": 0.33,

                        "score_neutral": 0.34

                    }

                    results.append(prediction)

                    break

            if index != total:

                print(

                    "\nWaiting 15 seconds before next request..."

                )

                time.sleep(5)

        print("\nGemini Classification Finished.\n")

        return results