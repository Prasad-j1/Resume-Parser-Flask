import os
from PDF_Handler import PDF_Converter
from OCR_Engine import OCR_Processor
from data_extractor import Resume_Data_Extractor
from Data_Storage import Data_Storage_Manager

"""This is the main module which will integrate and run all other modules.
   We just need to initialize given below class object and execute the run() for that obj.
   This project can take an input as a path of :-
                 1. A single Image
                 2. A single PDF
                 3. A folder containing many images & pdfs.
"""

class ResumeParserApp:
   
    IMAGE_EXT = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}
    PDF_EXT = {".pdf"}

    def __init__(self, path):
        self.path = path
        self.data_storage = Data_Storage_Manager()

    def run(self):
        files_to_process = self.get_files(self.path)
        parsed_data = []

        for file in files_to_process:
            info = self.process_file(file)
            if info:
                parsed_data.append(info)

        self.data_storage.save_to_excel(parsed_data)
        print("All resumes processed successfully!")

        return parsed_data

    # Detect folder or single file
    def get_files(self, path):
        if os.path.isdir(path):
            # Folder case
            print("Folder detected — scanning files...")
            files = []
            for f in os.listdir(path):
                full = os.path.join(path, f)
                if os.path.isfile(full):
                    ext = os.path.splitext(full)[1].lower()
                    if ext in self.IMAGE_EXT or ext in self.PDF_EXT:
                        files.append(full)
            return files

        elif os.path.isfile(path):
            # Single file case
            return [path]

        else:
            raise ValueError("The provided path is neither a file nor a folder.")

    # Process PDF or image
    def process_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()

        if ext in self.PDF_EXT:
            print(f"PDF detected: {file_path}")
            pdf_conv = PDF_Converter(file_path)
            images = pdf_conv.convert_to_images()

            ocr = OCR_Processor(images)
            text = ocr.extract_all()

        elif ext in self.IMAGE_EXT:
            print(f"Image detected: {file_path}")
            ocr = OCR_Processor([file_path])
            text = ocr.extract_all()

        else:
            print(f"Unsupported file skipped: {file_path}")
            return None

        extractor = Resume_Data_Extractor(text,file_path)
        info = extractor.extract_all()
        return info