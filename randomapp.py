import requests

#url we get after runing server

URL="http://127.0.0.1:8000/student_create"

#now we are just sending the python dictionary in the form of json

data ={

    'name':'shree',
    'email':'s@s.com',
    'city':'jammu',
}


#To convert python object to the json we use dumps method
# To use this method we need to import it first from json
import json 

json_data =json.dumps(data)

#we will send this data with a request


#before this we had used the GET method to retrieve/recieve data 
#here we are sending the data so just use the post method 

r =requests.post(url=URL, data= json_data)   #so here whatever response you get will be stored within r

#To extract the data we just initialize it and pass to r.json()
data=r.json()  
print(data)

