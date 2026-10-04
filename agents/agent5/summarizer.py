import re

from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained(
    "facebook/bart-large-cnn"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "facebook/bart-large-cnn"
)


def split_into_sentences(text):

    sentences = re.split(

        r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s',

        text

    )

    return [

        sentence.strip()

        for sentence in sentences

        if sentence.strip()

    ]


def make_chunks(

    sentences,

    chunk_word_limit=350

):

    chunks = []

    current_chunk = []

    current_word_count = 0

    for sentence in sentences:

        sentence_words = len(sentence.split())

        if (

            current_word_count + sentence_words

            > chunk_word_limit

            and current_chunk

        ):

            chunks.append(

                " ".join(current_chunk)

            )

            current_chunk = []

            current_word_count = 0

        current_chunk.append(sentence)

        current_word_count += sentence_words

    if current_chunk:

        chunks.append(

            " ".join(current_chunk)

        )

    return chunks


def get_context_sentences(

    chunk_text,

    n=2

):

    sentences = split_into_sentences(chunk_text)

    context = (

        sentences[-n:]

        if len(sentences) >= n

        else sentences

    )

    return " ".join(context)


def summarize_text(

    text,

    min_len=40,

    max_len=120

):

    inputs = tokenizer(

        text,

        return_tensors="pt",

        truncation=True,

        max_length=1024

    )

    summary_ids = model.generate(

        inputs["input_ids"],

        max_length=max_len,

        min_length=min_len,

        num_beams=4,

        length_penalty=2.0,

        no_repeat_ngram_size=3,

        early_stopping=True

    )

    return tokenizer.decode(

        summary_ids[0],

        skip_special_tokens=True

    )

def summarize_article(

    text,

    chunk_word_limit=350

):

    text = str(text)

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    # ---------------------------------------------------
    # Calculate Dynamic Summary Length
    # ---------------------------------------------------

    word_count = len(text.split())

    target_words = int(word_count * 0.25)

    target_words = max(target_words, 120)

    target_words = min(target_words, 350)

    final_min = int(target_words * 0.75)

    final_max = target_words

    print(f"\nArticle Words : {word_count}")

    print(f"Target Summary : {target_words} words")

    # ---------------------------------------------------

    sentences = split_into_sentences(text)

    chunks = make_chunks(

        sentences,

        chunk_word_limit

    )

    print(f"Chunks Created : {len(chunks)}")

    chunk_summaries = []

    context = ""

    for i, chunk in enumerate(chunks):

        print(

            f"Summarising Chunk {i+1}/{len(chunks)}"

        )

        if context:

            input_text = (

                f"Context: {context}\n\n"

                f"Article:\n{chunk}"

            )

        else:

            input_text = chunk

        try:

            summary = summarize_text(

                input_text,

                min_len=40,

                max_len=120

            )

            chunk_summaries.append(summary)

        except Exception as e:

            print(e)

        context = get_context_sentences(

            chunk,

            2

        )

    print("\nFinal Compression...")

    combined_summary = " ".join(chunk_summaries)

    try:

        final_summary = summarize_text(

            combined_summary,

            min_len=final_min,

            max_len=final_max

        )

    except Exception:

        final_summary = combined_summary

    return final_summary