from django.contrib import admin
from django.urls import path, include
from .views import *
from My_App import views
from rest_framework import routers
from rest_framework import urlpatterns
from My_App.views import StudentList, StudentDetail
import json

urlpatterns = [
    path('', views.index, name="index"),
    path('stud_list_view/',views.StudentList.as_view(),name='stud_list_view'),
# path('stud_detail_view/',views.StudentDetail.as_view(),name='stud_detail_view'),
    path('add/', views.add, name='add'),
    path('delete/<int:roll_num>/', views.delete, name="delete"),
    path('update/<int:roll_num>/', views.update, name="update"),
    path('json/',views.jsondata, name="jsondata"),
]

