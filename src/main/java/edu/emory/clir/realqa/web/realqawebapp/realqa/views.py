import json, urllib, urllib2, base64

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from realqa.models import *

#View all questions
def allQuestions(request):

    template_name = 'realqa/index.html'
    
	#request list of questions from API
    results = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request('http://realqa.mathcs.emory.edu/questions/')))))
    context = {'question_list' : results}
	
    # if user is logged in
    if 'apiToken' in request.session:
        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')

# View a particular question and its answers
def questionDetail(request, q_id):

    template_name = 'realqa/detail.html'
    
	# hit API and get detailed question data
    urlq = "http://realqa.mathcs.emory.edu/questions/" + str(q_id)
    question = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request(urlq)))))
    urla = "http://realqa.mathcs.emory.edu/questions/" + str(q_id) + "/answers/"
    answers = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request(urla)))))

    qa = {}
    qa['question'] = question
    qa['answers'] = answers 
	
    context = {'qa' : qa}

    if 'apiToken' in request.session:
        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')

# #Ask a question
# def askQuestion(request):
#
# 	#must be logged in
#     if 'apiToken' request.session:
#         data = {
#     	    "body"				 : request.POST['body'],
#             "tagnames"			 : request.POST['tags'],
#             "time_spent_editing" : request.POST['edit_time'],
#             "latitude"			 : request.POST['lat'],
#             "longitude" 		 : request.POST['long'],
#             "location_name" 	 : request.POST['loc']
#         }
#
#         json = json.dumps(data)
#         req = urllib2.Request('http://realqa.mathcs.emory.edu/questions/', json, request.session['apiToken'])
#
# 		return HttpResponseRedirect('/realqa/')
# 	else:
#         return HttpResponseRedirect('/realqa/login')
	
#Answer a question
def answerQuestion(request, q_id):

    if 'apiToken' in request.session:
        data = {
            "body"				:	request.POST['answer'],
            "time_spent_editing":	"2"
            }

        jsonstr = json.dumps(data)
        url = "http://realqa.mathcs.emory.edu/questions/" + str(q_id) + "/answers/"
        headers = {
                   'Content-Type': 'application/json',
                   'Authorization': 'Basic ' + request.session['auth']
                   }

        req = urllib2.Request(url, jsonstr, headers)

        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError, e:
            #TODO: if credentials are bad (redirect back with errors?)
            return HttpResponseRedirect('/realqa/%s/' % q_id) # HTTP RETURNS 500 error but still posts so we hacked the solution

         # if response is good
        else:
            return HttpResponseRedirect('/realqa/%s/' % q_id) # HTTP RETURNS 500 error but still posts so we hacked the solution


    else:
        return HttpResponseRedirect('/realqa/login')


def login(request):
    template_name = 'realqa/login.html'
    model = User

    # Login user and store API token session
    if request.method == 'POST':
        #TODO: validate, but not really

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
            request.session['auth'] = base64.b64encode(username + ":" + password)

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


