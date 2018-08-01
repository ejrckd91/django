#dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mysum(request, x, y=0, z=0):#모든 view함수는 첫번쨰 인자가 request
    #request: HttpRequest
    return HttpResponse(int(x) + int(y)+ int(z))#view의 인자로 넘겨 받은 값들은 모두 문자열
