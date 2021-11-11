from rest_framework import serializers

from .models import Student, Rishi

#we will now send of the data from the front endd with the use of 3rd party application



class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id' , 'name' , 'email' , 'city')

        name = serializers.CharField(max_length=500)
        email =serializers.EmailField(max_length=50)
        city = serializers.CharField(max_length=25)

#here we are just creating the deserializers but to act we need it to get from views...

def create(self,validate_data):
    return Student.objects.create(**validate_data)


#Now we are dealing with the update serializers here

class RishiSerializers(serializers.Serializer):
    employee_id=serializers.IntegerField()
    job_title=serializers.CharField(max_length=50)
    company=serializers.CharField(max_length=20)
        



