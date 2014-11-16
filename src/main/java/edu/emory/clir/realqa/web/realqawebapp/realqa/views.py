from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from realqa.models import Question, Answer

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'realqa/index.html'
    context_object_name = 'question_list'
    
    def get_queryset(self):
        """Return the last 10 published questions."""
        return Question.objects.order_by('-added_at')[:10]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'realqa/detail.html'
    def get_queryset(self):
        return Question.objects.filter(added_at__lte=timezone.now())