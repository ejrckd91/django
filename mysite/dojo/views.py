#dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def mysum(request, numbers):#모든 view함수는 첫번쨰 인자가 request
    #request: HttpRequest
    #numbers = "1/2/12/123/1234/123/121233"
    result = sum(map(int,numbers.split("/")))
    return HttpResponse(result)#view의 인자로 넘겨 받은 값들은 모두 문자열
