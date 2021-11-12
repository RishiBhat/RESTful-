from rest_framework import serializers

from .models import Rishi
class RishiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rishi
        fields = ('id' , 'employee_id' , 'job_title' , 'company')
    
    employee_id=serializers.IntegerField()
    job_title=serializers.CharField(max_length=50)
    company=serializers.CharField(max_length=20)

#now creating a function to update the data
def create(self,validate_data):
    return Rishi.objects.create(**validate_data)
   

#now for creating any update operation we need to implement update method 

def update(self,instance,validate_data):
    print('====================================================================>', instance.employee_id) 
    instance.employee_id=validate_data.get('employee_id',instance.employee_id )         #This means if user provides any data it will accept otherwise it will just take up the DB values
    print('////////////////////////////', instance.employee_id)                    #gets our current database value 
    instance.job_title=validate_data.get('job_title',instance.job_title)
    instance.company=validate_data.get('company',instance.company)
    
    #we need to save the instance

    instance.save()
    return instance