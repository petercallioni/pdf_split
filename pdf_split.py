from PyPDF2 import PdfFileWriter, PdfFileReader


class PdfSplitter:

    def __init__(self, source_pdf_path):
        self.source_pdf_path = source_pdf_path

    def split(self, pdf_output_dict: dict):
        """
        :param pdf_output_dict: a dictionary [string, int()] of the output file paths and what pages they should contain
        """

        source_pdf_reader = PdfFileReader(open(self.source_pdf_path, "rb"), strict=False)

        for key, value in pdf_output_dict.items():
            output = PdfFileWriter()
            for page in value:
                output.addPage(source_pdf_reader.pages[page])
            with open(key, "wb") as outputStream:
                output.write(outputStream)
