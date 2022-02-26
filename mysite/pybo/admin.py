from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
# 관리자 화면에서 제목으로 질문 검색
# Question 모델에 세부 기능을 추가할 수 있는 클래스 생성
# 제목 검색을 위한 search_fields 속성에 'subject' 추가

admin.site.register(Question, QuestionAdmin)

# Register your models here.
# 다른 장고 관리자 속성은 검색
