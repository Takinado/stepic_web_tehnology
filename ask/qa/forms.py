# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import get_object_or_404

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255, label='Вопрос')
    text = forms.CharField(widget=forms.Textarea, label='Текст вопроса')

    def save(self):
        if self._user.is_anonymous:
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author_id'] = self._user
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Текст ответа')
    question_id = forms.IntegerField(widget=forms.HiddenInput)

    def save(self):
        question = get_object_or_404(
            Question, pk=self.cleaned_data['question_id']
        )
        self.cleaned_data['question_id'] = question.id
        if self._user.is_anonymous():
            self.cleaned_data['author_id'] = 1
        else:
            self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
