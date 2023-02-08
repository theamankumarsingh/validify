import pandas as pd
import openpyxl

def dict_to_workbook(working_data_dict):
    df = pd.DataFrame(data=working_data_dict, index=[0])
    df = (df.T)
    df.to_excel('NGOs_Name_with_Address_bad.xlsx')

def workbook_to_dict(sheet_name):
    data_dict={}
    wb=openpyxl.load_workbook(sheet_name)
    sheet=wb['Sheet1']
    for row in range(2,sheet.max_row+1):
        data_dict[row-1]=sheet['B'+str(row)].value
    return data_dict

