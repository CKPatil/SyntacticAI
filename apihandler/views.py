from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response=requests.get('http://dummy.restapiexample.com/api/v1/employees',headers=headers).json

    return render(request,'home.html',{'name':response})
