# NOTE

## Serializer

```python
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
	class Meta:
        model = Post
        fields = '__all__'
```

## Router

```python
# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRoter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
 	path('', include(router.urls)),
]
```

## Http test

using `httpie`
`pip3 install httpie`

## Encode

python `json.dumps`는 querySet에 대한 serialize를 지원하지 않는다. 그러므로 `DjangoJSONEncoder`를 통해 커스텀 룰을 추가해줘야 한다.

```python
from json
from django.core.serializer.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model

query_set = get_user_model().objects.all()
json_string = json.dumps(query_set, cls=DjangoJSONEncoder) # also raised error
print(cls)

# use list comprehension
data = [
 	{'id': post.id, 'title': post.title} for post in Post.objects.all()
]
json.dumps(data, ensure_ascii=False) # do not need django json encoder
```

변환 Rule 지정해준다.

```python
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet

class MyJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, QuerySet):
            return tuple(ob)
        elif isinstance(obj, Post):
            return {'id': obj.id, 'title': obj.title, 'content': obj.content}
        elif hasattr(obj, 'as_dict'):
            return obj.as_dict()
        else:
            return super().default(obj) # use DjnagoJSONEncoder.default

data = Post.objects.all()
# now we can use our custom serializer
json.dumps(data, cls=MyJSONEncoder, ensure_ascii=False)
```
