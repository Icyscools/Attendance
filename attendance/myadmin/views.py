from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student(request):
    return HttpResponse("student")

def addstudent(request):
    return HttpResponse("addstudent")

def editstudent(request):
    return HttpResponse("editstudent")

def subject(request):
    return HttpResponse("subject")

def addsubject(request):
    return HttpResponse("addsubject")

def editsubject(request):
    return HttpResponse("editsubject")
