import functools
from multiprocessing.pool import ThreadPool

from PyPDF2 import PdfFileWriter, PdfFileReader


def main():
    record_count = 1355
    split_every = 5
    pdf_output_dict = {}
    input_pdf_path = "TEST.pdf"
    input_pdf = PdfFileReader(open(input_pdf_path, "rb"), strict=False)

    for i in range(1, record_count + 1):
        page_end = i * split_every
        pdf_output_dict[f"PDF_{i}.pdf"] = range(page_end - 5, page_end)

    split(input_pdf, pdf_output_dict)

    #   multithreaded split is actually way slower, due to opening the reader multiple times
    #   pool = ThreadPool(4)
    #   results = pool.map(functools.partial(split_parallel, input_pdf_path), pdf_output_dict.items())

    print(f"Done Writing {record_count} files.")


def split_parallel(input_pdf, pdf_output_dict):
    """
    This method is actually slower than non-parallel due to needing to open a PDF reader each time.

    :param input_pdf: the path o the source pdf to split
    :param pdf_output_dict: a dictionary [string, int()] of the output file paths and what pages they should contain
    """

    input_pdf_file_reader = PdfFileReader(open(input_pdf, "rb"), strict=False)
    print(f"{pdf_output_dict[0]}, {pdf_output_dict[1]}")
    output = PdfFileWriter()
    for page in pdf_output_dict[1]:
        output.addPage(input_pdf_file_reader.pages[page])
    with open(pdf_output_dict[0], "wb") as outputStream:
        output.write(outputStream)


def split(input_pdf_file_reader, pdf_output_dict: dict):
    """
    :param input_pdf_file_reader: the PdfFileReader the source pdf to split
    :param pdf_output_dict: a dictionary [string, int()] of the output file paths and what pages they should contain
    """

    for key, value in pdf_output_dict.items():
        output = PdfFileWriter()
        for page in value:
            output.addPage(input_pdf_file_reader.pages[page])
        with open(key, "wb") as outputStream:
            output.write(outputStream)


if __name__ == "__main__":
    main()
