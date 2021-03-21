from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#모델의 attr이 변경된 경우 migrate해주어야 함.
#model.objects.get은 단 하나의 object만 반환함, filter는 조건에 맞는 모든 쿼리를 가져옴
class Question(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='quthor_question')
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)

    voter=models.ManyToManyField(User,related_name='voter_question')
    def __str__(self):
        return self.subject

class Answer(models.Model):
    #when the Qustion removed, also answer removed
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_answer')
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    modify_date=models.DateTimeField(null=True,blank=True)
    voter=models.ManyToManyField(User,related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


