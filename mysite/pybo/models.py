# 파이보 : 질문과 답변을 할 수 있는 파이썬 게시판 서비스
# 질문과 답변에 해당되는 데이터 모델이 있어야 함

# 질문(question) 모델에 필요한 속성
# subject : 질문의 제목
# content : 질문의 내용
# create_date : 질문 작성 일시

# 답변(answer) 모델에 필요한 속성
# question : 질문
# content : 답변의 내용
# create_date : 답변을 작성한 일시

from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 제목 최대 200글자 -> 글자수의 길이가 제한된 Text : CharField 사용
# 내용 글자 수 상관X -> TextField
# 작성일시 -> 날짜, 시간 관계된 속성 : DateTimeField
# __str__ 메서드를 이용하여 id값 대신 제목 표시
# 모델에 메서드 추가시 makemigrations와 migrate를 수행할 필요x
# migrate 명령이 필요한 경우 : 모델의 속성이 변경되었을 떼

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

# shell -> q.answer_set을 사용하면 질문에 연결된 답변을 가져올 수 있다.
# 연결모델명_set : 질문 하나에 여러개의 답변 이 가능하므로 q.answer_set이 가능
# 답변 하나에 여러개의 질문이 있을 수 없음 : a.question_set 불가

# 기존 모델을 속성으로 연결 : ForeignKey
# on_delete=models.CASCADE : 질문이 삭제될 경우 답변도 함께 삭제

# Create your models here.
