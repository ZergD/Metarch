from pathlib import Path

import PyPDF2
import os
import pdfminer


class BusQuery:
    def __init__(self):
        print("BusQuery created...")
        self.name = "Metarch"

    def run(self):
        """
        Test with PyPDF2, works but the output needs a lot of work to get info we need out of it.
        Returns: None

        """
        print(f"{self.name} starting run function")

        # Path
        path_to_pdf = Path.cwd() / "metarch/ressources/express_1_Hiver_19_20.pdf"
        print("The file with path {} was found : {}".format(path_to_pdf, Path.is_file(path_to_pdf)))
        print("#######################################################################################################")

        pdf_file_obj = open(str(path_to_pdf), "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

        print(f"there are {pdf_reader.numPages} pages in this document")

        page_obj = pdf_reader.getPage(0)
        first_page_text = page_obj.extractText()
        print(first_page_text)

    def run2(self):
        """
        Test with
        Returns:

        """
        print(f"{self.name} starting run function")









