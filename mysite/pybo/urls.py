# 기존 config/urls.py 파일에 설정했던 내용과 별 차이 x
from django.urls import path
from . import views

app_name='pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]
# config/urls.py 파일에서 이미 pybo/로 시작하는 URL이 pybo/urls.py와 먼저 매핑됨
# = /pybo URL은 config/urls.py 파일에 매핑된 pybo/와 pybo/urls.py 파일에 매핑된 ''이 더해져 view.index 함수와 매핑됨

# URL 별칭
# http://localhost:8000/pybo/ URL은 index,
# http://localhost:8000/pybo/2 와 같은 URL에는 detail 이라는 이름을 부여

# pybo 앱 이외의 다른 앱이 프로젝트에 추가시
# 다른 앱에서 동일한 URL 별칭을 사용하면 중복 발생
# 문제 해결 위해 pybo/urls.py 파일에 네임스페이스를 의미하는 app_name 변수를 지정해야 함


