# blog 폴더내에 urls.py라는 파일을 생성하고 코드를 넣음

from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
]