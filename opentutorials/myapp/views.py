from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("welcome to index page.")


def create(request):
    return HttpResponse("create page")


def read(request):
    return HttpResponse("read page")
