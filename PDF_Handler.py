from pdf2image import convert_from_path
import re

"""Takes a PDF and converts it into a list of images for further processing."""

class PDF_Converter():
    __path_poppler = None
   
    def __init__(self,pdf_path):
        self.__pdf_path = pdf_path
        self.__images = []
       
    def convert_to_images(self,dpi = 300):
        self.__images = convert_from_path(pdf_path, dpi=150, first_page=1, last_page=2)
        return self.__images
