from django.contrib import admin

from django.contrib.admin import ModelAdmin

from .models import Question, Answer


class QuestionAdmin(ModelAdmin):
    class Meta:
        model = Question


class AnswerAdmin(ModelAdmin):
    class Meta:
        model = Answer

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
