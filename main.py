from pdf_split import PdfSplitter
from gui import GUI


def main():
    record_count = 1000
    split_every = 3
    pdf_output_dict = {}
    input_pdf_path = "TEST.pdf"
    pdf_splitter = PdfSplitter(input_pdf_path)

    for i in range(1, record_count + 1):
        page_end = i * split_every
        pdf_output_dict[f"PDF_{i}.pdf"] = range(page_end - split_every, page_end)

    pdf_splitter.split(pdf_output_dict)
    print(f"Done Writing {record_count} files.")


def main_gui():
    gui = GUI()
    gui.show_gui()


if __name__ == "__main__":
    main_gui()
