from django.contrib import admin

from .models import Rishi  
# Register your models here.



@admin.register(Rishi)
class RishiAdmin(admin.ModelAdmin):
    list_display=['id','employee_id','job_title','company']
