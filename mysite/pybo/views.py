from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
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
   question = get_object_or_404(Question, pk=question_id)
   context = {'question': question}
   return render(request, 'pybo/question_detail.html', context)

# detail 함수 호출시 전달되는 매개변수가 question_id 추가
# question_id에는 URL 매핑시 저장된 question_id가 전달달
# get_object_or_404(Question, pk=question_id)로 변경
# pk : Question 모델의 primary key(id)

def answer_create(request, question_id):
   """
   pybo 답변등록
   """
   question = get_object_or_404(Question, pk=question_id)
   question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
   return redirect('pybo:detail', question_id=question.id)

# answer_create 함수의 매개변수 question_id는 URL 매핑에 의해 그 값이 전달됨
#    ex) http://locahost:8000/pybo/answer/create/2/ 라는 페이지를 요청하면
#       question_id에는 2라는 값 전달됨
# 답변 등록시 텍스트창에 입력한 내용은 answer_create 함수의 첫번째 매개변수 requset를 통해 읽기 가능
#    requset.POST.get('content') : POST로 전송된 폼(form) 데이터 항목 중 content 값을 의미
# 답변 생성 위해 qustion.answer_set.create를 사용
#    qustion.answer_set.create : 질문의 답변
#    -> ForeginKey로 질문과 답변이 연결되어있어 사용 가능

# 답변 저장 다른 방법
# def answer_create(request, question_id):
#    """
#    pybo 답변등록
#    """
#    question = get_object_or_404(Question, pk=question_id)
#    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
#    answer.save()
#    return redirect('pybo:detail', question_id=question.id)

















