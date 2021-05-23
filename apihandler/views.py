from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request):
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
    response=requests.get('http://dummy.restapiexample.com/api/v1/employees',headers=headers).json

    return render(request,'home.html',{'name':response})

def update(request):
    empname=request.GET["empname"]
    empsal=request.GET["empsal"]
    empage=request.GET["empage"]

    url='http://dummy.restapiexample.com/api/v1/create'
    payload=json.dumps({"name":empname,"salary":empsal,"age":empage})
    headers = {'Content-Type': 'application/json','Accept':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

    response = requests.post(url,data=payload,headers=headers)

    return render(request,'home.html',{'temp':response})