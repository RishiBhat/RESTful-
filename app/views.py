import json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt     #we are just taking up the csrf token in the exempt form 


# Create your views here.
@csrf_exempt
def student_create(request):

    if request.method=='POST':                         #we just now checked wether the request is post or not
        json_data = request.body
                                                      #here wee are just taking up  the json_data body
        stream = io.BytesIO(json_data)                #converting the json body to the string
        pythondata = JSONParser().parse(stream)       #converting the string to the python data
        serializer = StudentSerializers(data=pythondata)   #converting the python data to the complex data to the db 
        
        if serializer.is_valid():                   #performing the validaition
            serializer.save()                       #data in serializer we save
            res = {'msg': 'Data inserted'}          
            json_data =JSONRenderer().render(res)                               ##this lines shall be ommitted with the json response
            return HttpResponse(json_data, content_type='application/json')
            #return JsonResponse(serializer.data)     #we just take json response as there is no need of 2 diff lines we just need to take up Jsonresponse(serializer.varname)
            #by default safe is false so no need to initialize it here



        #if the data does not get validated it will come in this section
        json_data =JSONRenderer().render(serializer.errors)      #we are taking the errors which does not get validate and save it in the error property
        return HttpResponse(json_data, content_type='application/json')    



#------------------------------------------------------------------------------------------------------------------------------
                                        #now we are just creating the other module Rishi and updating the json data

from app.models import Rishi
from app.serializers import RishiSerializers

def rishi_create(request):

    if request.method=="GET":           #we need to get the data so we use the GET
        json_data = request.body
        print("===================================================================================>",json_data)

        stream=io.BytesIO(json_data)
        print(json_data)
        pythondata=JSONParser().parse(stream)

        id = pythondata.get('id',None)           #now we will see the python data includes the id or not, python data has everything in it....
        
        if id is not None:
            ris=Rishi.objects.get(id=id)          #we take up the following id with the GET and take it in the python data
            rishiserialized =RishiSerializers(ris) #takes up all of our data
            json_data = JSONRenderer().render(rishiserialized.data)
            return HttpResponse(json_data, content_type='application/json')

        #including this because if we not give up a id value to it we just take up all of the objects
        ris = Rishi.objects.all()
        rishiserialized = RishiSerializers(ris, many=True)
        print("====================================================////>", ris)
        json_data = JSONRenderer().render(rishiserialized.data)
        print(json_data)
        return HttpResponse(json_data, content_type='application/json')
    