from django.db import models

# Create your models here.

#we will be sending the data through 3rd party app with the serializers help now




class Student(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Rishi(models.Model):

    employee_id=models.IntegerField()
    job_title=models.CharField(max_length=50)
    company=models.CharField(max_length=20)


    def __str__(self):
        return self.job_title