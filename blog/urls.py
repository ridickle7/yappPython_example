from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]

# ^ : "시작"
# post/     : post를 포함해야한다
# (?P<pk>)  : 괄호안에 넣은 모든 것을 변수 pk에 저장
# [0-9]     : 숫자 0부터 9까지 하나의 숫자만 있다
# +         : 최소 하나의 숫자 이상이 있어야 한다
