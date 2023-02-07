#imports
import openpyxl
import preparation

#import sheet from workbook
wb=openpyxl.load_workbook('NGOs_Name_with_Address.xlsx')
sheet=wb['Sheet1']

#pre-processing
dataset,data_dict=preparation.prepare(sheet)