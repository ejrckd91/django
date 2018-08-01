#blog/urls.py
from django.conf.urls import url
from . import views
#개발도중에는 서버를 항상 켜두기.
#추가 입력이 필요할 때는 쉘을 하나 더 열어서 필요한 커맨드입력(linux에서)
urlpatterns = [
    url(r'^$', views.post_list), #<< 저건 함수자체를 넘겨주는것 함수처리를 넘겨주는게 아님
]