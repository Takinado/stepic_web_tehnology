from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question, Answer
from .forms import AskForm, AnswerForm

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
    page, paginator = paginate(request, questions)
    paginator.baseurl = reverse('index') + '/?page='

    return render(request, 'index.html', {
        'questions':    page.object_list,
        'page':         page,
        'paginator':    paginator,
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


def question_detail(request, pk, *args, **kwargs):
    question = get_object_or_404(Question, id=pk)
    answers = question.answer_set.all()
    form = AnswerForm(initial={'question': str(pk)})
    return render(request, 'question_detail.html', {
        'question': question,
        'answers':  answers,
        'form': form,
    })


def question_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            # url = question.get_url(question.pk)
            url = reverse('question_detail', args=[question.id])
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html', {
        'form': form
    })


def question_answer_add(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            # url = answer.question.get_url(answer.question.pk)
            url = reverse('question_detail', args=[answer.question.id])
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')
