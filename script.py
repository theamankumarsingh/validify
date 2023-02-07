#imports
import openpyxl

wb=openpyxl.load_workbook('NGOs_Name_with_Address.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
