from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO

from pathlib import Path


class BusQuery:
    def __init__(self):
        print("BusQuery created...")
        self.name = "Metarch"

    def pdf_to_text(self, path):
        print(f"{self.name} starting bus pdf to text")
        manager = PDFResourceManager()
        retstr = BytesIO()
        # layout = LAParams(all_texts=True)
        layout = LAParams()
        text_converter = TextConverter(manager, retstr, laparams=layout)
        filepath = open(path, 'rb')
        interpreter = PDFPageInterpreter(manager, text_converter)
        for page in PDFPage.get_pages(filepath, check_extractable=True):
            interpreter.process_page(page)

        text = retstr.getvalue()
        filepath.close()
        text_converter.close()
        retstr.close()
        return text

    def run(self):
        path_to_pdf = Path.cwd() / "metarch/ressources/express_1_Hiver_19_20.pdf"
        print("The file with path {} was found : {}".format(path_to_pdf, Path.is_file(path_to_pdf)))
        text = self.pdf_to_text(str(path_to_pdf))
        print(text)
