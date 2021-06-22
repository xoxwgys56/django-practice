# Progress Note

## Part 1 ~ 3

create supderuser

```plain
username: admin
pwd: 1111
```

done.

## Part 4

> https://docs.djangoproject.com/ko/3.2/intro/tutorial04/

```html
<form action="{% url 'polls:vote' question.id %}" method="post"></form>
```

ask `post` using `form` tag. those code are included in `views.py`.  
이것은 장고의 구조와 일치되는 부분이다. MVC 패턴을 사용하여, 비즈니스 로직을 view에 구현하는 것.

```python
selected_choice = question.choice_set.get(pk=request.POST['choice'])
```

done.

### TODO

- [ ] find what is measure way to post request from frontend.
  - in this case use `form` tag.
  - basic implementation RESTful using django.
- [ ] review part 4
  - why use `form` tag.
  - if not, use JS?

till now. use GET and POST method only.

## Part 5

> https://docs.djangoproject.com/ko/3.2/intro/tutorial05/

Let's learn about testing!  
`django.test.TestCase`를 이용해 유닛테스트를 한다.

```shell
# run test
$ python manage.py test polls

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
was_published_recently() returns False for questions whose pub_date
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/dwkim/dw/_project/django-practice/src/polls/tests.py", line 17, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

### Django test client

```shell
python manage.py shell
```

```python
# inside of venv
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

response = client.get('/')
# Not Found: /
response.status_code
# 404

from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
# 200
response.content
# b'\n<ul>\n  \n  <!-- <li><a href="/polls/2/">What&#x27;s that?</a></li> -->\n  <li><a href="/polls/2/">What&#x27;s that?</a></li>\n  \n</ul>\n\n'
response.context['latest_question_list']
# <QuerySet [<Question: What's that?>]>
```

장고에서는 테스트 코드가 비대해지는 것을 우려하지 말라고 말합니다.

## Part 6

add `/static/polls/style.css`. that's all.

## Part 7

modify admin. `fields`를 `fieldsets`로 변경했다.

> django 예약어인가?

```python
fields = ['pub_date', 'question_text']

# to change

fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
```

### 관련된 객체 추가

OK, 우리는 Question 관리자 페이지를 가지고 있습니다. 그러나, Question은 여러 개의 Choice들을 가지고 있음에도, admin 페이지는 선택 사항을 표시하지 않습니다. 이것을 해결할 수 있는 2가지 방법이 있습니다.

```python
# polls/admin.py
admin.site.register(Choice)
```

관리자 페이지 커스터마이징.

> [여기](https://docs.djangoproject.com/ko/3.2/intro/reusable-apps/) 진행 중.
