#dojo/views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def mysum(request, numbers):#모든 view함수는 첫번쨰 인자가 request
    #request: HttpRequest
    #numbers = "1/2/12/123/1234/123/121233"
    result = sum(map(int,numbers.split("/")))
  
    return HttpResponse(result)#view의 인자로 넘겨 받은 값들은 모두 문자열

def hello(request, name, age):
    
    
    return HttpResponse('안녕하세요. {}님. {}살이시네요.'.format(name,age))
    
def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    <p>여러분의 파이썬 &장고 페이스메이커가 되어드리겠습니다.</p>
    '''.format(name=name))

def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name' : name})

def post_list3(request):
    return JsonResponse({
        'massage' : '안녕 장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }, json_dumps_params={'ensure_ascii' : False})

#0807 4가지 함수기반 뷰
#장고기본편 View OVERVIEW 15분쯤 보면 xls(엑셀)파일 다운로드하는방법등 여러가지 나옴.
