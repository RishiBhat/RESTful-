import requests
import json


URL= " http://127.0.0.1:8005/rishi_create"

#this function will request for the data, if the user gives specific ID he gets data or if he exludes any he gets the full data

def get_data(id=None):             #if no value he gets in ID it will be NONE
    
    data={}                        #taking up a empty dictionary 
    
    if id is not None:            #if id get any value ex...1,2,233,4,4,,4,4,5,5,,5,56,7,7,...........
        data={'id':id}             #if we get any ID value it will get stored in the data variable
                                   #This data will be send from client to the server
    json_data = json.dumps(data)   #converting our python data to the  json dict using dumpss ... 
                                   #sending the data from client to the server
    
    r=requests.get(url=URL, data=json_data)

    data=r.json()                  #taking up the json data, extracting.........

    print(data) 

get_data(2)