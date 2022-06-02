import ctypes
import os
import tkinter
from tkinter import filedialog

from pdf_split import PdfSplitter


class GUI:
    def __init__(self):
        self.execute_button = None
        self.page_count_entry = None
        self.record_count_entry = None
        self.destination_pdf_entry = None
        self.destination_pdf_button = None
        self.source_pdf_entry = None
        self.source_pdf_button = None

    def create_gui(self) -> tkinter.Tk:
        window = tkinter.Tk()
        window.title = "PDF Splitter"
        window.geometry("400x150")

        self.source_frame(window).pack(fill="both", expand=True)
        self.destination_frame(window).pack(fill="both", expand=True)
        self.fixed_items_frame(window).pack(fill="both", expand=True)
        self.controls_frame(window).pack(fill="both", expand=True)

        return window

    def source_frame(self, tk: tkinter.Tk) -> tkinter.Frame:
        source_frame = tkinter.Frame(tk, bg="green", padx=5, pady=5)

        source_pdf_label = tkinter.Label(master=source_frame, text="Source PDF:")
        source_pdf_label.grid(column=0, row=0)

        self.source_pdf_entry = tkinter.Entry(master=source_frame)
        self.source_pdf_entry.grid(column=1, row=0, sticky="nsew")

        self.source_pdf_button = tkinter.Button(master=source_frame, text="Find", command=self.select_file)
        self.source_pdf_button.grid(column=2, row=0)

        source_frame.grid_columnconfigure(0, weight=0, pad=5)
        source_frame.grid_columnconfigure(1, weight=1, pad=5)
        source_frame.grid_columnconfigure(2, weight=0, pad=5)

        return source_frame

    def destination_frame(self, tk: tkinter.Tk) -> tkinter.Frame:
        destination_frame = tkinter.Frame(tk, bg="green", padx=5, pady=5)
        destination_pdf_label = tkinter.Label(master=destination_frame, text="Destination Folder:")
        destination_pdf_label.grid(column=0, row=0)

        self.destination_pdf_entry = tkinter.Entry(master=destination_frame)
        self.destination_pdf_entry.grid(column=1, row=0, sticky="nsew")

        self.destination_pdf_button = tkinter.Button(master=destination_frame, text="Find", command=self.select_folder)
        self.destination_pdf_button.grid(column=2, row=0)

        destination_frame.grid_columnconfigure(0, weight=0, pad=5)
        destination_frame.grid_columnconfigure(1, weight=1, pad=5)
        destination_frame.grid_columnconfigure(2, weight=0, pad=5)
        return destination_frame

    def fixed_items_frame(self, tk: tkinter.Tk) -> tkinter.Frame:
        fixed_items_frame = tkinter.Frame(tk, bg="green", padx=5, pady=5)

        record_count_label = tkinter.Label(master=fixed_items_frame, text="Record Count:")
        record_count_label.grid(column=0, row=0)

        self.record_count_entry = tkinter.Entry(master=fixed_items_frame)
        self.record_count_entry.grid(column=1, row=0, sticky="nsew")

        page_count_label = tkinter.Label(master=fixed_items_frame, text="Pages Per Record:")
        page_count_label.grid(column=2, row=0)

        self.page_count_entry = tkinter.Entry(master=fixed_items_frame)
        self.page_count_entry.grid(column=3, row=0, sticky="nsew")

        fixed_items_frame.grid_columnconfigure(0, weight=0, pad=5)
        fixed_items_frame.grid_columnconfigure(1, weight=1, pad=5)
        fixed_items_frame.grid_columnconfigure(2, weight=0, pad=5)
        fixed_items_frame.grid_columnconfigure(3, weight=1, pad=5)
        return fixed_items_frame

    def controls_frame(self, tk: tkinter.Tk) -> tkinter.Frame:
        controls_frame = tkinter.Frame(tk, bg="green", padx=5, pady=5)

        self.execute_button = tkinter.Button(master=controls_frame, text="Split", command=self.execute_split)
        self.execute_button.grid(column=0, row=0)

        controls_frame.grid_columnconfigure(0, weight=0, pad=5)
        return controls_frame

    def set_text(self, entry: tkinter.Label, text: str):
        entry.delete(0, tkinter.END)
        entry.insert(0, text)

    def show_gui(self):
        self.create_gui().mainloop()

    def select_file(self):
        self.set_text(self.source_pdf_entry, filedialog.askopenfilename(filetypes=[("PDFs", "pdf")]))

    def select_folder(self):
        self.set_text(self.destination_pdf_entry, filedialog.askdirectory())

    def finished_dialog(self):
        show_message("Done.", "Done.", 0)

    def execute_split(self):
        pdfSplitter = PdfSplitter(self.source_pdf_entry.get())

        pdf_output_dict = {}
        for i in range(1, int(self.record_count_entry.get()) + 1):
            page_end = i * int(self.page_count_entry.get())
            output_path = outputFilename = os.path.join(self.destination_pdf_entry.get(), f"PDF_{i}.pdf")
            pdf_output_dict[output_path] = range(page_end - int(self.page_count_entry.get()), page_end)

        pdfSplitter.split(pdf_output_dict)

        self.finished_dialog()


def show_message(title: str, message: str, style: int) -> ctypes.windll.user32.MessageBoxW:
    """
    Shows a message box using the standard windows dll.
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
