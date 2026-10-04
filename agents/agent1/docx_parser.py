from docx import Document


class DocxParser:

    @staticmethod
    def extract_paragraphs(file_path):
        """
        Reads a DOCX file and returns a list of non-empty paragraphs.
        """

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if text:
                paragraphs.append(text)

        return paragraphs