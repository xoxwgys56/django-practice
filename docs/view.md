# About Django View

## 1. FBV

Functional-Base View

```python
# urls.py
urlpatterns = [
    path('', views.index, name='index'),
]

# views.py
def index(request):
    if request.method == 'POST':         
        # POST 요청일경우 
    else:         
        # POST 요청이 아닐 경우
```

## 2. CBV

Class-Base View

```python
# urls.py
urlpatterns = [
    path('', IndexView.as_view()),
]

#views.py
from django.views.generic import View


class IndexView(View):
    model = 사용할 모델이 있다면

    def get(self, request):
        # Get 리퀘스트 일경우
    def post(self, request):
        # POST 리퀘스트 일경우
```

### Generic View

자주 사용하는 기능을 `generic view`를 통해 제공한다. MDN에서는 클래스 기반 뷰를 아예 제네릭 뷰로 설명하고 있다. 아래는 그 예시 코드.

```python
from django.views import generic

# ListView를 사용한다.
class BookListView(generic.ListView):
    model = Book
```

---

## References

- basics
  - https://velog.io/@yejin20/DjangoFBV-%EC%99%80-CBV
  - https://dingrr.com/blog/post/djangofbvs-vs-cbvs-%ED%95%A8%EC%88%98%ED%98%95-%EB%B7%B0-vs-%ED%81%B4%EB%9E%98%EC%8A%A4%ED%98%95-%EB%B7%B0
  - https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Generic_views#%EB%B7%B0(%ED%81%B4%EB%9E%98%EC%8A%A4_%EA%B8%B0%EB%B0%98)
  - https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/#generic-views-of-objects
- diff about TemplateView vs ListView
  - https://stackoverflow.com/questions/25335154/what-is-the-difference-between-using-templateview-and-listview-in-django