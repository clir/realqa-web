from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json, urllib, urllib2

from realqa.models import *
from realqa.forms import UserForm

# Create your views here.

API_URL = "http://realqa.mathcs.emory.edu/"

# View for the home page Dashboard where the questions can be viewed.
class IndexView(generic.ListView):
    template_name = 'realqa/index.html'
    context_object_name = 'question_list'

    # URL to hit API endpoint
    url = ''.join([API_URL, 'recommended_questions_by_freshness/'])

    def get_queryset(self):
        """Return the last 10 published questions."""
        return Question.objects.order_by('-added_at')[:10]


# View for when you click on a question, can view all the answers.	
class DetailView(generic.DetailView):
    model = Question
    template_name = 'realqa/detail.html'

    # Orders the answers based on time submitted.
    def get_queryset(self):
        return Question.objects.filter(added_at__lte=timezone.now())

# class LoginView(generic.ListView):
#     template_name = 'realqa/login'
#
#     # Login and store API token
#     def login(request):
#         if request.method == 'POST':
#             form = LoginForm(request.POST)
#
#             if form.is_valid():
#                 # process the data in form.cleaned_data as required
#
#                 # redirect to new url
#                 return HttpResponseRedirect('realqa/index.html')
#
#         else:
#             form = LoginForm()
#
#         return render(request, 'realqa/login.html', {'form': form})


# Logout only possible when user is already logged in, redirects to a page telling user they have been logged out.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/realqa/logout/')
