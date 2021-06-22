# How do I implement RESTful in Django?

## why RESTful?

### answer of Darrel Miller

> [stackoverflow answer](https://stackoverflow.com/questions/1368014/why-do-we-need-restful-web-services)

#### minimize of coupling

서버와 클라이언트 간의 커플링 최소화.  
이것의 예시는 많은 클라이언트를 관리하지 않거나, 서버를 정기적으로 업데이트할 때 클라이언트의 업데이트가 필요하지 않도록 하는 것.  

low level에서 이것을 구현하는 것은 쉽지 않을 것이다. (쉽지 않다는 내용) 그럼에도 불구하고 hypermedia를 쉽게 찾을 수 있고, 서버 변화에도 클라이언트가 회복력 있게 버틸 수 있게 해준다.  

그는 아래와 같은 질문을 던진다.

> 웹 브라우저 또한 REST 클라이언트이다.

- Why do you not need to do a browser update when someone changes some html on a web site?
- Why can I add a complete new set of pages to a web site and the "client" can still access those new pages without an update?
- Why do I not need to provide a "service-description-language" to the web browser to tell it when it goes to http://example.org/images/cat that the return type will be a jpeg image and when you go to http://example.org/description/cat the return type will be text/html?
- Why can I use a web browser to visit sites that did not exist when the browser was released? How can the client know about these sites?

### answer of 유동호님

> [유동호님 Medium](https://berkbach.com/%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EC%82%B4%ED%8E%B4%EB%B3%B4%EB%8A%94-rest-api-79422dfc0a7d)

```plain
/show/categoryname    => 카테고리 이름을 나타내기
/add/categoryname     => 카테고리 이름을 추가
/change/categoryname  => 카테고리 이름을 변경
/delete/categoryname  => 카테고리 이름을 삭제
```

이렇게 요청을 받는 API를 구성하면, 기능이 추가될수록 url이 길어지게 됩니다. 이 때 각 기능 표현을 HTTP method를 이용합니다.  

```plain
http method: GET      url:   /categoryname    => 카테고리 이름을 나타내기
http method: POST     url:   /categoryname    => 카테고리 이름을 추가
http method: PUT      url:   /categoryname    => 카테고리 이름을 변경
http method: DELETE   url:   /categoryname    => 카테고리 이름을 삭제
```

#### use Django REST framework

```shell
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework', # add
]
```

#### Serializer

![serializer template diff](https://miro.medium.com/max/700/1*AjXUSAQ5WPHi2lvfRKD08g.jpeg)

`template`와 다르게 `JSON`으로 매핑해줍니다. 아래의 코드에서는 `ModelSerializer`를 사용합니다.

```python
# api/serializers.py
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'subtitle',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
```

## Follow official tutorial

> [quick start](https://www.django-rest-framework.org/tutorial/quickstart/)

```shell
mkdir tutorial
# 폴더와 가상환경 만드는 과정 생략.

pip install django
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

## References

- basics
  - https://berkbach.com/restful-api-in-django-16fc3fb1a238
  - https://berkbach.com/%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EC%82%B4%ED%8E%B4%EB%B3%B4%EB%8A%94-rest-api-79422dfc0a7d
  - https://www.django-rest-framework.org/tutorial/quickstart/
- why do we need
  - https://medium.com/@whj2013123218/django-rest-api%EC%9D%98-%ED%95%84%EC%9A%94%EC%84%B1%EA%B3%BC-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-a95c6dd195fd
  - https://stackoverflow.com/questions/1368014/why-do-we-need-restful-web-services