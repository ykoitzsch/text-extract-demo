from haystack.nodes import PDFToTextConverter


class ExtractionService:
    def __init__(self):
        self.converter = PDFToTextConverter(
            remove_numeric_tables=False, valid_languages=["en", "de", "pl"])

    def extract_from_pdf(self, file_path):
        return self.converter.convert(file_path=file_path, meta=None)[0]
