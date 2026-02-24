from pdf2image import convert_from_path
import re

"""Takes a PDF and converts it into a list of images for further processing."""

class PDF_Converter():
    __path_poppler = r'C:\Program Files\poppler-25.12.0\Library\bin'
   
    def __init__(self,pdf_path):
        self.__pdf_path = pdf_path
        self.__images = []
       
    def convert_to_images(self,dpi = 300):
        self.__images = convert_from_path(self.__pdf_path,dpi,poppler_path = PDF_Converter.__path_poppler)
        return self.__images