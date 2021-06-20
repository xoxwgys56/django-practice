# Progress Note

## Part 1 ~ 3

done.

## Part 4

| https://docs.djangoproject.com/ko/3.2/intro/tutorial04/

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

## Part 5

| https://docs.djangoproject.com/ko/3.2/intro/tutorial05/
