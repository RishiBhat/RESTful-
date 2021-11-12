from django.db import models

# Create your models here.
#Here we are working with the  class based views


class Rishi(models.Model):

    employee_id=models.IntegerField()
    job_title=models.CharField(max_length=50)
    company=models.CharField(max_length=20)

    def __str__(self):
        return self.job_title