import pytesseract
"""To Extract text from given images"""

class  OCR_Processor():
   
    def __init__(self,images):
        self.__images = images
       
    def extract_all(self):           # Extract text and return
        text = ''
        for img in self.__images:
            text += pytesseract.image_to_string(img)
        return text