#dojo/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    #하나의함수(mysum)이 꼭 한가지 패턴에 매핑 될 필요 없음. 
    #디폴트인자를 넣어두면 1개,2개,3개일 때도 전부 매핑가능
    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),

]
