from pyexpat.errors import messages
from wsgiref import validate
from django.shortcuts import redirect,render
from django.http import HttpResponse
from .admin import StudentAdmin
from .models import Student
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Student
from django.http import JsonResponse
from django.urls import reverse
from django.views import View
from django .conf import settings
# from rest_framework import viewsets , permissions
from rest_framework .response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework import status
from My_App import serializers
from django.urls import reverse
from django .conf import settings
import json
from rest_framework .response import Response
from rest_framework.views import APIView

#import mysql.connector as mcdb
# conn = mcdb.connect(host="localhost",user="root",passwd="Sasikala@123", database="Student")
# print("Successfully connected to database")
# cur = conn.cursor()
# Create your views here.
def jsondata(request):
       data = list(Student.objects.values())
       return JsonResponse(data,safe = False)

def index(request):
    stud = Student.objects.all()
    return render(request,'index.html',{'stud': stud})

def add(request):
    if request.method == 'POST':
        data = request.POST
        stud = Student.objects.create(
           roll_num = data['roll_num'],
           name = data['name'],
           standard = data['standard'],
           city = data['city'],
           phoneno = data['phoneno']
        )
        # going to the home page
        return redirect('index')
    return render(request,'add.html')

def delete(request,roll_num):
    stud = Student.objects.get(roll_num=roll_num)
    stud.delete()
    return redirect(reverse('index'))

def update(request, roll_num):
    stud = Student.objects.get(roll_num=roll_num)
    if request.method =='POST':
        roll_num = request.POST['roll_num']
        name=request.POST['name']
        standard=request.POST['standard']
        city=request.POST['city']
        phoneno=request.POST['phoneno']

        stud.roll_num = request.POST['roll_num']
        stud.name = name
        stud.standard = standard
        stud.city = city
        stud.phoneno= phoneno
        stud.save()
    return render(request,'update.html', {'stud': stud})
    stud.save()

class StudentList(APIView):
    def get(self,request):
        stud = Student.objects.all()
        serializer = StudentSerializer(stud,many=True)
        return Response(serializer.data)
         
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class StudentDetail(APIView):
    def stud_object(self, roll_num):
        try:
            return Student.objects.get(roll_num=roll_num)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
    
    def get(self, request, roll_num):
        stud = Student.objects.all(roll_num)
        serializer = StudentSerializer(stud)
        return Response(serializer.data)
    
    def put(self, request, roll_num):
        stud = Student.stud_object(roll_num)
        serializer = StudentSerializer(stud, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, roll_num): 
        stud = Student.stud_object(roll_num)
        stud.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
