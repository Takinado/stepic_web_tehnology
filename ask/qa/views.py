from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question, Answer

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 100
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page) # Page
    except PageNotAnInteger:
        #page = paginator.page(1)
        raise Http404
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    page.page_range = paginator.page_range
    return page


def question_list_all(request, *args, **kwargs):
    questions = Question.objects.all()
    page = paginate(request, questions)
    page.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


def new(request, *args, **kwargs):
    questions = Question.objects.new()
    page = paginate(request, questions)
    page.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


def popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    page.baseurl = '/popular/?page='
    return render(request, 'index.html', {
        'questions':  page.object_list,
        'page':       page,
    })


def question_details(request, pk, *args, **kwargs):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.all().filter(question=pk)
    return render(request, 'question_detail.html', {
        'question': question,
        'ansters':  answers,
    })
