#imports
import openpyxl
import preparation
import clean
import finalization

#write sheet from workbook
wb=openpyxl.load_workbook('NGOs_Name_with_Address.xlsx')
sheet=wb['Sheet1']

#pre-processing
dataset,data_dict=preparation.prepare(sheet)
working_data_dict=preparation.filter_bad_data(data_dict)

print(working_data_dict)

#cleaning
#autoclean

#clean (manual)
working_data_dict=clean.start_manual(working_data_dict,"NGOs_Name_with_Address_working.xlsx",skip=False)

#post-processing
data_dict=finalization.change(working_data_dict,data_dict)
dataset=finalization.modify(dataset,data_dict)
test_res=finalization.check(dataset,skip=False)

#write sheet to workbook
wb_new = openpyxl.Workbook()
sheet_new = wb_new['Sheet']
for row in range(len(dataset)):
    sheet_new['A'+str(row+1)]=dataset[row][1]
    sheet_new['B'+str(row+1)]=dataset[row][2]
    sheet_new['C'+str(row+1)]=dataset[row][3]
    sheet_new['D'+str(row+1)]=dataset[row][4]
    sheet_new['E'+str(row+1)]=dataset[row][5]
if len(test_res):
    wb_new.create_sheet('Test')
    sheet_new = wb_new['Test']
    for row in range(len(test_res)):
        sheet_new['A'+str(row+1)]=test_res[row][0]
        sheet_new['B'+str(row+1)]=test_res[row][1]
        sheet_new['C'+str(row+1)]=test_res[row][2]
wb_new.save('NGOs_Name_with_Address_cleaned.xlsx')