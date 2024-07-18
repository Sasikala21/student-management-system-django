from rest_framework import serializers
from .models import Student
#from dataclasses import field
#from pyexpat import model

#create a model serializer
class StudentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Student
         fields = ['roll_num', 'name', 'standard', 'city', 'phoneno']

