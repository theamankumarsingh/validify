#imports
import openpyxl
import preparation
import finalization

#write sheet from workbook
wb=openpyxl.load_workbook('NGOs_Name_with_Address.xlsx')
sheet=wb['Sheet1']

#pre-processing
dataset,data_dict=preparation.prepare(sheet)

#cleaning

#post-processing
dataset=finalization.modify(dataset,data_dict)

#write sheet to workbook
wb_new = openpyxl.Workbook()
sheet_new = wb_new['Sheet']
for row in range(len(dataset)):
    sheet_new['A'+str(row+1)]=dataset[row][1]
    sheet_new['B'+str(row+1)]=dataset[row][2]
    sheet_new['C'+str(row+1)]=dataset[row][3]
    sheet_new['D'+str(row+1)]=dataset[row][4]
    sheet_new['E'+str(row+1)]=dataset[row][5]
wb_new.save('NGOs_Name_with_Address_cleaned.xlsx')