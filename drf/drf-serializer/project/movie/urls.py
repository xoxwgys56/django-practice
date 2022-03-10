from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet

router = routers.DefaultRouter()
router.register(r"movie", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
