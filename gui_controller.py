import ctypes
import os

from gui import GUI
from pdf_split import PdfSplitter


class GuiController:

    def __init__(self):
        self.gui = None
        self.pdf_splitter = PdfSplitter()
        self.record_count = None
        self.page_count = None
        self.source_pdf = None
        self.destination_pdf = None

    def execute_split(self, record_count, page_count, source_pdf, destination_pdf):
        self.record_count = record_count
        self.page_count = page_count
        self.source_pdf = source_pdf
        self.destination_pdf = destination_pdf

        pdf_output_dict = {}
        for i in range(1, int(self.record_count) + 1):
            page_end = i * int(self.page_count)
            output_path = outputFilename = os.path.join(self.destination_pdf, f"PDF_{i}.pdf")
            pdf_output_dict[output_path] = range(page_end - int(self.page_count), page_end)

        self.pdf_splitter.split(self.source_pdf, pdf_output_dict)

    def show_message(self, title: str, message: str, style: int) -> ctypes.windll.user32.MessageBoxW:
        """
        Shows a message box using the standard Windows dll.
        :param title:
        :param message:
        :param style: Styles:
        0 : OK
        1 : OK | Cancel
        2 : Abort | Retry | Ignore
        3 : Yes | No | Cancel
        4 : Yes | No
        5 : Retry | Cancel
        6 : Cancel | Try Again | Continue
        :return:
        """
        return ctypes.windll.user32.MessageBoxW(0, message, title, style)
