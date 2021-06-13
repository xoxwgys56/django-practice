import datetime

from django.db import models
from django.utils import timezone


"""
below codes makes django

- 이 앱을 위한 데이터베이스 스키마 생성(`CREATE TABLE` 문)
- `Question`과 `Choice` 객체에 접근하기 위한 Python 데이터베이스 접근 API를 생성
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
