from PyPDF2 import PdfFileWriter, PdfFileReader


class PdfSplitter:

    def split(self, source_pdf_path: str, pdf_output_dict: dict):
        """
        :param source_pdf_path: the path of the original file to be split
        :param pdf_output_dict: a dictionary [string, int()] of the output file paths and what pages they should contain
        """

        source_pdf_reader = PdfFileReader(open(source_pdf_path, "rb"), strict=False)

        for key, value in pdf_output_dict.items():
            output = PdfFileWriter()
            for page in value:
                output.addPage(source_pdf_reader.pages[page])
            with open(key, "wb") as outputStream:
                output.write(outputStream)
