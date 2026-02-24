import pandas as pd
import os

"""To Store the list of dictionaries in an excel file"""

class Data_Storage_Manager():
   
    def __init__(self,Output_File = r"Parsed_Resumes.xlsx"):
        self.__Output_File = Output_File
       
#Either create new Excel or concat in previously created excel.
    def save_to_excel(self,data_list):
        df = pd.DataFrame(data_list)
        # if os.path.exists(self.__Output_File):
        #     existing = pd.read_excel(self.__Output_File)
        #     df = pd.concat([existing,df], ignore_index = True)
        df.to_excel(self.__Output_File, index = False)