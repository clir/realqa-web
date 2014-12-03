import json, urllib, urllib2

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from realqa.models import *


def allQuestions(request):

    template_name = 'realqa/index.html'
    
    results = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request('http://realqa.mathcs.emory.edu/questions/')))))
    context = {'question_list' : results}
	
    # if user is logged in
    if 'apiToken' in request.session:
        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')

# View for when you click on a question, can view all the answers.
def questionDetail(request, q_id):

    template_name = 'realqa/detail.html'
    
    urlq = "http://realqa.mathcs.emory.edu/questions/" + str(q_id)
    question = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request(urlq)))))
    urla = "http://realqa.mathcs.emory.edu/questions/" + str(q_id) + "/answers/"
    answers = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request(urla)))))

    qa = {}
    qa['question'] = question
    qa['answers'] = answers 
	
    context = {'qa' : qa}
    # hit API and get detailed question data
	
    if 'apiToken' in request.session:
        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')



def login(request):
    template_name = 'realqa/login.html'
    model = User

    # Login user and store API token session
    if request.method == 'POST':
        # validation?

        # get request data
        username = request.POST['username']
        password = request.POST['password']

        # seralize into JSON
        data = {
            "username": username,
            "password": password
        }
        data = json.dumps(data)

        # hit API endpoint
        req = urllib2.Request('http://realqa.mathcs.emory.edu/api-token-auth/', data, {'Content-Type': 'application/json'})

        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError, e:
            #TODO: if credentials are bad (redirect back with errors?) 
            return HttpResponse(e)

         # if response is good
        else:
            # store session var and redirect to index
            response = HttpResponseRedirect('/realqa/')
            apiToken = json.load(result)['token']
            request.session['apiToken'] = apiToken

            return response


    # Render login page
    elif request.method == 'GET':
        # if user has a stored session var, then no need to log in
        if 'apiToken' in request.session:
            return render_to_response('realqa/index.html', {'apiToken': request.session['apiToken']})

        return render(request, template_name)


# Logout only possible when user is already logged in, redirects to a page telling user they have been logged out.
def logout(request):

    if 'apiToken' in request.session:
        del request.session['apiToken']

    return HttpResponseRedirect('/realqa/login')


