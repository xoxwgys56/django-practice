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

## REST vs SOAP

> [Red Hat doc](https://www.redhat.com/ko/topics/integration/whats-the-difference-between-soap-rest)

### RESTful

RESTful이 반드시 `JSON`으로 반환되어야 하는 것은 아니다. (하지만 권장된다고 보인다.) `JSON`은 어떠한 프로그래밍 언어로든 읽을 수 있고, 인간과 기계가 모두 읽을 수 있으며, 경량화되어 있기 때문에 선호되는 메시지 형식입니다.  
RESTful은 프로토콜이 아닙니다.

#### 애플리케이션이 갖춰야 하는 6가지 요소

1. 클라이언트, 서버, 리소스로 구성된 클라이언트-서버 아키텍처가 필요합니다.
2. 요청이 통과하는 서버에 클라이언트 콘텐츠가 저장되지 않는 [스테이트리스(stateless)](https://www.redhat.com/ko/topics/cloud-native-apps/stateful-vs-stateless) 클라이언트-서버 커뮤니케이션이 필요합니다. 대신 세션의 상태에 대한 정보가 클라이언트에 저장됩니다.
3. 일부 클라이언트-서버 간 상호 작용의 필요성을 제거할 캐시 가능 데이터가 필요합니다.
4. 애플리케이션 요구 사항별로 다른 형식이 아닌, 표준화된 형식으로 정보를 전송할 수 있도록 구성 요소 간 통합된 인터페이스가 필요합니다. REST를 처음으로 제시한 [Roy Fielding](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)은 이를 "REST 아키텍처 스타일을 다른 네트워크 기반 스타일과 차별화하는 핵심적인 기능"이라고 설명합니다.
5. 클라이언트-서버 간의 상호 작용을 계층적으로 조정할 수 있도록 계층화된 시스템 제약이 필요합니다.
6. 실행 가능한 코드를 전송해 서버가 클라이언트의 기능을 확장할 수 있게 해주는 코드 온디맨드가 필요합니다. 단, 가시성이 감소할 수 있으므로 이는 선택적 가이드라인입니다.

### SOAP

Simple Object Access Protocol은 다른 언어로 다른 플랫폼에서 빌드된 애플리케이션이 통신할 수 있도록 설계된 최초의 표준 프로토콜입니다.  
프로토콜이기 때문에 복잡성과 오버헤드를 증가시키는 빌트인 룰을 적용하므로, 페이지 로드 시간이 길어질 수 있습니다. 그러나 이러한 표준은 builtin compliance를 제공한다는 의미이므로, 기업에서 선호하는 방식이기도 합니다. (보안 규정들을 준수할 수 있도록 기준점을 제공한다는 의미로 보인다.)  

> builtin compliance include [api security](https://www.redhat.com/ko/topics/security/api-security) and ACID

일반적인 웹 서비스 사양에는 다음이 포함됩니다.

- 웹 서비스 보안(WS-security): 토큰이라고 불리는 고유 식별자를 통해 메시지를 보호하고 전송하는 방식을 표준화합니다.
WS-ReliableMessaging: 불안정한 IT 인프라로 전송되는 메시지 간 오류 처리를 표준화합니다.
- 웹 서비스 주소지정(WS-addressing): 심층 네트워크에 라우팅 정보를 유지관리하는 대신, SOAP 헤더 내에 메타데이터로 해당 정보를 패키징합니다.
- 웹 서비스 기술 언어(WSDL): 웹 서비스가 무엇을 하는지, 해당 서비스의 시작과 종료 위치를 기술합니다.

SOAP는 XML 형태로 메시지를 반환한다. SOAP API에 대해 완료된 요청은 브라우저에서 캐싱할 수 없으므로, API로 재전송하지 않는 한 이후에 접근할 수 없다. <- ?

### 비교

대부분의 레거시 시스템에서 SOAP를 준수하며, REST는 그보다 뒤에 고려하거나 웹 기반 시나리오에서의 더 빠른 대안으로 여기는 경우가 많습니다. REST는 유연한 구현을 제공하는 가이드라인 세트고, SOAP는 XML 메시징과 같은 특정 요건이 있는 프로토콜입니다.

REST API는 경량화되어 있기 때문에 사물 인터넷(IoT), 모바일 애플리케이션 개발, 서버리스(servreless) 컴퓨팅과 같이 보다 새로운 컨텍스트에 이상적입니다. SOAP 웹 서비스는 많은 기업에서 필요로 하는 기본 보안과 트랜잭션 컴플라이언스를 제공하지만, 이로 인해 좀 더 무거운 경향이 있습니다. 또한 Google Maps API와 같은 대부분의 퍼블릭 API는 REST 가이드라인을 따릅니다.

### SOA

SOA는 SOAP랑 아무 상관없어 보인다. MSA와 연관있다고 보는게 맞는 것 같다.

> more about [SOA](https://www.redhat.com/ko/topics/cloud-native-apps/what-is-service-oriented-architecture)

## References

- basics
  - https://berkbach.com/restful-api-in-django-16fc3fb1a238
  - https://berkbach.com/%EA%B0%84%EB%8B%A8%ED%95%98%EA%B2%8C-%EC%82%B4%ED%8E%B4%EB%B3%B4%EB%8A%94-rest-api-79422dfc0a7d
  - https://www.django-rest-framework.org/tutorial/quickstart/
- why do we need
  - https://medium.com/@whj2013123218/django-rest-api%EC%9D%98-%ED%95%84%EC%9A%94%EC%84%B1%EA%B3%BC-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%82%AC%EC%9A%A9-%EB%B0%A9%EB%B2%95-a95c6dd195fd
  - https://stackoverflow.com/questions/1368014/why-do-we-need-restful-web-services
- diff with SOAP
  - https://www.redhat.com/ko/topics/integration/whats-the-difference-between-soap-rest
  - https://www.redhat.com/ko/topics/cloud-native-apps/what-is-service-oriented-architecture