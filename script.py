#imports
import openpyxl
import preparation
import finalization

#write sheet from workbook
wb=openpyxl.load_workbook('NGOs_Name_with_Address.xlsx')
sheet=wb['Sheet1']

#pre-processing
dataset,data_dict=preparation.prepare(sheet)
working_data_dict=preparation.filter_bad_data(data_dict)

#cleaning

#post-processing
data_dict=finalization.change(working_data_dict,data_dict)
dataset=finalization.modify(dataset,data_dict)
test_res=finalization.check(dataset)

#write sheet to workbook
wb_new = openpyxl.Workbook()
wb_new.create_sheet('Test')
sheet_new = wb_new['Sheet']
for row in range(len(dataset)):
    sheet_new['A'+str(row+1)]=dataset[row][1]
    sheet_new['B'+str(row+1)]=dataset[row][2]
    sheet_new['C'+str(row+1)]=dataset[row][3]
    sheet_new['D'+str(row+1)]=dataset[row][4]
    sheet_new['E'+str(row+1)]=dataset[row][5]
sheet_new = wb_new['Test']
for row in range(len(test_res)):
    sheet_new['A'+str(row+1)]=test_res[row][0]
    sheet_new['B'+str(row+1)]=test_res[row][1]
    sheet_new['C'+str(row+1)]=test_res[row][2]
wb_new.save('NGOs_Name_with_Address_cleaned.xlsx')