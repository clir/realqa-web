from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from realqa.models import *
from realqa.forms import UserForm

# Create your views here.

# View for the home page Dashboard where the questions can be viewed.
class IndexView(generic.ListView):
    template_name = 'realqa/index.html'
    context_object_name = 'question_list'
    
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
		

# Logout only possible when user is already logged in, redirects to a page telling user they have been logged out.
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/realqa/logout/')
	
