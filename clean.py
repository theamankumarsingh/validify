import pandas as pd
import openpyxl

def dict_to_workbook(working_data_dict,data_problem_dict,workbook_name):
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    keyss=list(working_data_dict.keys())
    keyss.sort()
    row=2
    #Headings
    sheet['A1']="Key No."
    sheet['B1']="Website"
    sheet['C1']="Problem"
    for key in keyss:
        sheet['A'+str(row)]=key
        sheet['B'+str(row)]=working_data_dict[key]
        if data_problem_dict[key]==():
            sheet['C'+str(row)]="autofix"
        else:
            sheet['C'+str(row)]=str(data_problem_dict[key])
        row+=1
    wb.save(workbook_name)

def workbook_to_dict(workbook_name):
    data_dict={}
    wb=openpyxl.load_workbook(workbook_name)
    sheet=wb['Sheet']
    for row in range(2,sheet.max_row+1):
        data_dict[sheet['A'+str(row)].value]=sheet['B'+str(row)].value
    return data_dict

def start_manual(working_data_dict,data_problem_dict,workbook_name,skip=True):
    if skip:
        return working_data_dict
    print("Starting manual cleaning ...")
    dict_to_workbook(working_data_dict,data_problem_dict,workbook_name)
    input("Please edit the file "+workbook_name+" and save it before proceeding. Press Enter to continue ...")
    return workbook_to_dict(workbook_name)