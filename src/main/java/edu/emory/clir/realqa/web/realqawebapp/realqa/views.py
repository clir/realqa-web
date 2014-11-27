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
		
def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
		else:
			print user_form.errors
	else:
		user_form = UserForm()
	return render_to_response(
		'realqa/register.html',
		{'user_form': user_form, 'registered': registered}, context
		)

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/realqa/')
            else:
                return HttpResponse("Invalid login")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('realqa/login.html', {}, context)
		
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/realqa/logout/')