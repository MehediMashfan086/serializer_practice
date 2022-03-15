from django.http import HttpResponse
from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

# Model-Object: single student data
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)                         #complex_data
    serializer = StudentSerializer(stu)                       #python_data
    json_data = JSONRenderer().render(serializer.data)        #json_data
    
    return HttpResponse(json_data, content_type = 'application/json')

# Query-Set: All Students Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    
    return HttpResponse(json_data, content_type = 'application/json')

