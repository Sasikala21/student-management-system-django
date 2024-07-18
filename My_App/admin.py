from django.contrib import admin
from My_App.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list=["roll_num","name","standard","city","phoneno"]

admin.site.register(Student, StudentAdmin)
