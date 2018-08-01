from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html') #경로앞에 app이름(blog) 써줘야함 왜인지는 template관리에서