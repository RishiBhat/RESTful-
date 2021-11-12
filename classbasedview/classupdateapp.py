#Reminder:: This can be any any third party application, so it is just for the testing purpose which we use over here

import requests
import json

URL= " http://127.0.0.1:8001/employee"


def get_data(id=None):             
    data={}                         
    if id is not None:            #if id get any value ex...1,2,233,4,4,,4,4,5,5,,5,56,7,7,...........
        data={'id':id}             #if we get any ID value it will get stored in the data variable
                                   #This data will be send from client to the server
    json_data = json.dumps(data)   #converting our python data to the  json dict using dumpss ... 
                                   #sending the data from client to the server
    
    r=requests.get(url=URL, data=json_data)

    data=r.json()                  #taking up the json data, extracting.........

    print(data) 

#get_data()


def post_data():
    data = {
        'employee_id':'777',
        'job_title':'C++',
        'company':'TechSmart',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

post_data()


# now will update the above details so commented the post_data() fx()

def update_data():

    data = {
        
        #we need to provide the ID if we wanna update the required value
        'id':5,
        'employee_id':'8888',
        'company':'Gnani.ai', 
        'job_title':'Senior Developer'
    }
   
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)    #in update we have put request & read we have the post request
    data = r.json()
    print(data)

#update_data()

#now we will perform the delete data 

def delete_data():
    data ={ 'id': 4}     #now we just need to give the specific ID to delete the data we do not require in our db....
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)    #Now we use the delete request to del. the specific record from our db...
    data = r.json()
    print(data)

#delete_data()