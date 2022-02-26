from django.shortcuts import render, get_object_or_404
from .models import Question
# from django.http import HttpResponse

#def index(request):
#    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def index(request):
   """
   pybo 목록 출력
   """
   question_list = Question.objects.order_by('-create_date')
   context = {'question_list': question_list}
   return render(request, 'pybo/question_list.html', context)

# render 함수 : 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수
# = question_list 데이터를 pybo/question_list.html 파일에 적용하여 HTML을 리턴
# pybo/question_list.html : 템플릿
# 템플릿 : HTML파일과 비슷하지만 장고에서 사용하는 태그를 사용할 수 있는 HTML 파일

def detail(request, question_id):
   """
   pybo 내용 출력
   """
   question = get_object_or_404(id=question_id, pk=question_id)
   context = {'question': question}
   return render(request, 'pybo/question_detail.html', context)

# detail 함수 호출시 전달되는 매개변수가 question_id 추가
# question_id에는 URL 매핑시 저장된 question_id가 전달달
# get_object_or_404(Question, pk=question_id)로 변경
# pk : Question 모델의 primary key(id)