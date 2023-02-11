import requests
from progressbar import progressbar

header = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
}

time_out=60

def prepare(sheet,duplicates=True):
    dataset=[]
    data_dict={}
    index=1
    for row in range(2,sheet.max_row+1):
        if sheet['E'+str(row)].value==None or sheet['E'+str(row)].value=="Not Available":
            continue
        dataset.append((index,sheet['A'+str(row)].value,sheet['B'+str(row)].value,sheet['C'+str(row)].value,sheet['D'+str(row)].value,sheet['E'+str(row)].value))
        data_dict[index]=sheet['E'+str(row)].value
        index+=1
    dataset,data_dict=remove_duplicates(dataset,data_dict,skip=duplicates)
    return dataset,data_dict

def filter_bad_data(data_dict):
    filter_res={}
    problem_res={}
    print("Filtering websites ...")
    for i in progressbar(range(len(data_dict))):
        web_url=data_dict[i+1] 
        try:
            response = requests.get(web_url,headers=header,timeout=time_out)
            stat_code=response.status_code
        except Exception as exception:
            filter_res[i+1]=web_url
            problem_res[i+1]=(1,type(exception).__name__)
            continue;
        if not(stat_code == 200):
            filter_res[i+1]=web_url
            problem_res[i+1]=(0,stat_code)
    return filter_res, problem_res

def remove_duplicates(dataset, data_dict, skip):
    if skip:
        return dataset, data_dict
    #remove keys
    for row in range(len(dataset)):
        dataset[row]=dataset[row][1:]
    #remove duplicates while preserving order
    dataset2=[]
    data_dict2={}
    for element in dataset:
        if element not in dataset2:
            dataset2.append(element)
    #add keys
    for row in range(len(dataset2)):
        data_dict2[row+1]=dataset2[row][4]
        dataset2[row]=(row+1,)+dataset2[row]
    return dataset2, data_dict2