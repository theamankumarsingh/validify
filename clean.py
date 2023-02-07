import pandas as pd

def dict_to_workbook(working_data_dict):
    df = pd.DataFrame(data=working_data_dict, index=[0])
    df = (df.T)
    df.to_excel('NGOs_bad_data.xlsx')

def workbook_to_dict(working_data_dict):
    xls = ExcelFile('NGOs_bad_data.xlsx')
    df = xls.parse(xls.sheet_names[0])
    working_data_dict = df.to_dict()
    return working_data_dict

