from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, QuestionManager

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_all(reqiest, *args, **kwargs):
    output = Question.objects.all()
    return HttpResponse(output)


def new(reqiest, *args, **kwargs):
    output = Question.objects.new()
    return HttpResponse(output)


def popular(reqiest, *args, **kwargs):
    output = Question.objects.popular()
    return HttpResponse(output)
