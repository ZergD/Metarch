from pathlib import Path

import PyPDF2
import os
import pdfminer


class BusQuery:
    def __init__(self):
        print("BusQuery created...")
        self.name = "Metarch"

    def run_works_manages_to_read_pdf(self):
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

    def run(self):
        """
        Test with
        Returns:

        """
        print(f"{self.name} starting run function")

        url = "https://www.ratp.fr/horaires-bus?network-current=busratp&networks=busratp&line_busratp=259&name_line_busratp=Saint-Germain-En-Laye+RER+%2F+Nanterre-Anatole+France&id_line_busratp=B259&id_t_line_busratp=&line_noctilien=&name_line_noctilien=&id_line_noctilien=&id_t_line_noctilien=&stop_point_busratp=Jaures&type=now&departure_date=15%2F01%2F2020&departure_hour=11&departure_minute=45&op=Rechercher&is_mobile=&form_build_id=form-7ePstc1FyFoNlx5G3llUHdQlfp3VeQxayuYUj4gIzY8&form_id=scheduledform"
