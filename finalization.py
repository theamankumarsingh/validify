def modify(dataset, data_dict):
    #modify dataset
    for row in range(len(dataset)):
        dataset[row]=list(dataset[row])
        dataset[row][5]=data_dict[dataset[row][0]]
        dataset[row]=tuple(dataset[row])
    return dataset