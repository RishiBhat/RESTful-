from django.contrib import admin

# Register your models here.
from .models import Student, Rishi



@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','email']

@admin.register(Rishi)
class RishiAdmin(admin.ModelAdmin):
    list_display=['id','employee_id','job_title','company']




