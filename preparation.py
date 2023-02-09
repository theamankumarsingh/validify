import requests
from progressbar import progressbar

header = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
}

def prepare(sheet):
    dataset=[]
    data_dict={}
    for row in range(2,sheet.max_row+1):
        dataset.append((row-1,sheet['A'+str(row)].value,sheet['B'+str(row)].value,sheet['C'+str(row)].value,sheet['D'+str(row)].value,sheet['E'+str(row)].value))
        data_dict[row-1]=sheet['E'+str(row)].value
    return dataset,data_dict

def filter_bad_data(data_dict):
    filter_res={}
    problem_res={}
    print("Filtering websites ...")
    for i in progressbar(range(len(data_dict))):
        web_url=data_dict[i+1] 
        if web_url==None or web_url=="Not Available":
            continue;
        else:
            try:
                response = requests.get(web_url,headers=header)
                stat_code=response.status_code
            except Exception as exception:
                filter_res[i+1]=web_url
                problem_res[i+1]=(1,type(exception).__name__)
                continue;
            if not(stat_code == 200):
                filter_res[i+1]=web_url
                problem_res[i+1]=(0,stat_code)
    return filter_res, problem_res