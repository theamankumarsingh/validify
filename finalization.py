import requests
from progressbar import progressbar

header = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
}

def modify(dataset, data_dict):
    #modify dataset
    for row in range(len(dataset)):
        dataset[row]=list(dataset[row])
        dataset[row][5]=data_dict[dataset[row][0]]
        dataset[row]=tuple(dataset[row])
    return dataset

def check(dataset):
    #check if websites are valid
    test_res=[]
    print("Checking websites...")
    for i in progressbar(range(len(dataset))):
        element=dataset[i]
        if element[5]==None or element[5]=="Not Available":
            test_res.append((element[5],"Skip",""))
            continue;
        else:
            try:
                response = requests.get(element[5],headers=header)
                stat_code=response.status_code
            except Exception as exception:
                test_res.append((element[5],"exception",type(exception).__name__))
                continue;
            if stat_code == 200:
                test_res.append((element[5],"good",str(stat_code)))
            else:
                test_res.append((element[5],"bad",str(stat_code)))
    return test_res