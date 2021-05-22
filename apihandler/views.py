from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    a=request.get['http://dummy.restapiexample.com/api/v1/employees']

    return render(request,'home.html',{'name':a})
