def prepare(sheet):
    dataset=[]
    data_dict={}
    for row in range(2,sheet.max_row+1):
        dataset.append((row-1,sheet['A'+str(row)].value,sheet['B'+str(row)].value,sheet['C'+str(row)].value,sheet['D'+str(row)].value,sheet['E'+str(row)].value))
        data_dict[row-1]=sheet['E'+str(row)].value
    return dataset,data_dict