"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from pybo import views <- pybo 앱에 관련한 것들은 pybo 앱 디렉터리 하위에 위치해야

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
]
# pybo/에 대한 url매핑 : pybo/로 시작하는 페이지를 요청하면 pybo/urls.py 파일의 매핑 정보를 읽어서 처리
# pybo/로 시작하는 URL을 추가해야 할 때 config/urls 파일을 수정할 필요없이 pybo/urls.py 파일을 수정하면 됨