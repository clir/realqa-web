from django.contrib import admin
from realqa.models import Question, Answer
from django.utils.regex_helper import Choice
from random import choice

# Register your models here.
class AnswerInLine(admin.StackedInline):
    model = Answer
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]
    

admin.site.register(Question, QuestionAdmin)