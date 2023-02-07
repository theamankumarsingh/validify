import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
}

def isValidURL(str):
 
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")
     
    # Compile the ReGex
    p = re.compile(regex)
 
    # If the string is empty
    # return false
    if (str == None):
        return False
 
    # Return if the string
    # matched the ReGex
    if(re.search(p, str)):
        return True
    else:
        return False
 

def check(data_dict):
    for key in data_dict:
        val = data_dict.get(key)
        print(val)
        # Check if valid URL
        if isValidURL(val):
            print("VALID")
            if requests.get(val, headers=headers).status_code == 200:
                print("good")
                response = requests.get(val, headers=headers)
                print(response)
                print(response.status_code)
            else:
                print("bad")
        # If not valid URL
        else:
            print("Not valid URL")
            print(val)

