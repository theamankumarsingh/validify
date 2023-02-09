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

def change(working_data_dict, data_dict):
    #apply changes to data_dict
    for key in working_data_dict:
        data_dict[key]=working_data_dict[key]
    return data_dict

def check(dataset, skip=False):
    #check if websites are valid
    if skip:
        return []
    test_res=[]
    print("Checking websites ...")
    for i in progressbar(range(len(dataset))):
        element=dataset[i]
        if element[5]==None or element[5]=="Not Available":
            test_res.append((element[0],element[5],"skip",""))
            continue;
        else:
            try:
                response = requests.get(element[5],headers=header)
                stat_code=response.status_code
            except Exception as exception:
                test_res.append((element[0],element[5],"exception",type(exception).__name__))
                continue;
            if stat_code == 200:
                test_res.append((element[0],element[5],"good",str(stat_code)))
            else:
                test_res.append((element[0],element[5],"bad",str(stat_code)))
    return test_res

def diff(original_data_diff, working_data_diff, problem_data_diff, skip=True):
    if skip:
        return []
    diff_res=[]
    for key in original_data_diff.keys():
        if original_data_diff[key]!=working_data_diff[key]:
            if problem_data_diff[key]==():
                diff_res.append((key,original_data_diff[key],working_data_diff[key],"auto"))
            else:
                diff_res.append((key,original_data_diff[key],working_data_diff[key],"manual"))
    return diff_res
