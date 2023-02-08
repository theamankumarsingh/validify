import pandas as pd
import openpyxl

def dict_to_workbook(working_data_dict,workbook_name):
    df = pd.DataFrame(data=working_data_dict, index=[0])
    df = (df.T)
    df.to_excel(workbook_name)

def workbook_to_dict(workbook_name):
    data_dict={}
    wb=openpyxl.load_workbook(workbook_name)
    sheet=wb['Sheet1']
    for row in range(2,sheet.max_row+1):
        data_dict[row-1]=sheet['B'+str(row)].value
    return data_dict

def start_manual(working_data_dict,workbook_name,skip=True):
    if skip:
        return working_data_dict
    print("Starting manual cleaning...")
    dict_to_workbook(working_data_dict,workbook_name)
    input("Please edit the file "+workbook_name+" and save it before proceeding. Press Enter to continue...")
    return workbook_to_dict(workbook_name)