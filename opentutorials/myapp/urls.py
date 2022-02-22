from django.urls import path
from myapp.views import *


urlpatterns = [
    path("", index),
    path("create/", create),
    path("read/<id>/", read),
    path("delete/", delete),
    path("update/", update),
]
