# 기존 config/urls.py 파일에 설정했던 내용과 별 차이 x
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
]
# config/urls.py 파일에서 이미 pybo/로 시작하는 URL이 pybo/urls.py와 먼저 매핑됨
# = /pybo URL은 config/urls.py 파일에 매핑된 pybo/와 pybo/urls.py 파일에 매핑된 ''이 더해져 view.index 함수와 매핑됨