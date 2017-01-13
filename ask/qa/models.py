# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    added_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    rating = models.IntegerField(blank=True, verbose_name='Рейтинг')
    author = models.ForeignKey(User, related_name='author', verbose_name='Автор')
    likes = models.ManyToManyField(User, blank=True, related_name='likes', verbose_name='Лайкнувшие')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.TextField(verbose_name='текст')
    added_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    question = models.ForeignKey(Question, verbose_name='Вопрос')
    author = models.ForeignKey(User, verbose_name='Автор')

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'