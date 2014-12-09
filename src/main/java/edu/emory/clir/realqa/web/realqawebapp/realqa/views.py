import json, urllib, urllib2, base64, hashlib

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views import generic
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from random import randint

from realqa.models import *

#View all questions
def allQuestions(request):

    template_name = 'realqa/index.html'

    # if user is logged in
    if 'apiToken' in request.session:

        # request list of questions from API
        results = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request('http://realqa.mathcs.emory.edu/questions/')))))

        i = 0
        for str in results['results']:
            taglist = str['tagnames'].split()
            results['results'][i]['tagnames'] = taglist
            i += 1

        context = {'question_list': results}

        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')		

		
def getURL(x):
	return {
		'0': 'http://realqa.mathcs.emory.edu/recommended_questions_by_freshness/',
		'1': 'http://realqa.mathcs.emory.edu/recommended_questions_by_relevance/', 
		'2': 'http://realqa.mathcs.emory.edu/recommended_questions_by_answer_count/',
		'3': 'http://realqa.mathcs.emory.edu/recommended_questions_by_location/',
		'4': 'http://realqa.mathcs.emory.edu/recommended_questions_by_popularity/', 
		'5': 'http://realqa.mathcs.emory.edu/asked_questions/',
		'6': 'http://realqa.mathcs.emory.edu/subscribed_questions/',
		'7': 'http://realqa.mathcs.emory.edu/answered_questions/'
	}.get(x, 'http://realqa.mathcs.emory.edu/questions/')

	
def allQuestionsSort(request, sort):

    url = getURL(sort)
    results = json.loads(json.dumps(json.load(urllib2.urlopen(urllib2.Request(url, None, {'Authorization':'Basic ' + request.session['auth']})))))
	
    if sort == '5' or sort == '6' or sort == '7':
        template_name = 'realqa/index.html'
        i = 0
        for str in results['results']:
            taglist = str['tagnames'].split()
            results['results'][i]['tagnames'] = taglist
            i += 1
			
    else:
        template_name = 'realqa/index2.html'
        for result in results['results']:
		    taglist = result['content_object']['tagnames'].split()
		    result['content_object']['tagnames'] = taglist
			
    context = {'question_list': results}

    return render(request, template_name, context) 


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
def askQuestion(request):

    query = request.POST['ask']
    taglist = [word for word in query.split() if word.startswith('#')]
    f_taglist = []
    for tag in taglist: 
        f_taglist.append(tag[1:])

    #loclist = [word for word in query.split() if word.startswith('@')]

    questionlist = [word for word in query.split() if word not in taglist] #and word not in locs
    tags = ' '.join(f_taglist)
    #locs = ' '.join(loclist)
    question = ' '.join(questionlist)

    #must be logged in
    if 'apiToken' in request.session:
        data = {
            "body"				 : question,
            "tagnames"			 : tags,
            "time_spent_editing" : randint(40, 77), 
            "latitude"			 : randint(0, 90), 
            "longitude" 		 : randint(0, 180), 
            "location_name" 	 : []
        }

        jsonstr = json.dumps(data)
        headers = {
                   'Content-Type': 'application/json',
                   'Authorization': 'Basic ' + request.session['auth']
                    }
        url = "http://realqa.mathcs.emory.edu/questions/"
        req = urllib2.Request(url, jsonstr, headers)

        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError, e:
            #TODO: if credentials are bad (redirect back with errors?)
            return HttpResponseRedirect('/realqa/success') # HTTP RETURNS 500 error but still posts so we hacked the solution
         # if response is good
        else:
            return HttpResponseRedirect('/realqa/success') 
    else:
        return HttpResponseRedirect('/realqa/login')


#Answer a question
def answerQuestion(request, q_id):

    if 'apiToken' in request.session:
        data = {
            "body"				:	request.POST['answer'],
            "time_spent_editing":	randint(40, 77) #TODO: change this
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
            return HttpResponseRedirect('/realqa/questions/%s/' % q_id) # HTTP RETURNS 500 error but still posts so we hacked the solution
         # if response is good
        else:
            return HttpResponseRedirect('/realqa/questions/%s/' % q_id)
    else:
        return HttpResponseRedirect('/realqa/login')

	
def upvote(request, q_id, id):

    headers = {
           'Content-Type': 'application/json',
           'Authorization': 'Basic ' + request.session['auth']
           }
		   
    url = "http://realqa.mathcs.emory.edu/nodes/" + str(id) + "/vote?vote_type=up" 

    req = urllib2.Request(url, "", headers)
    
    result = urllib2.urlopen(req)
    return HttpResponseRedirect('/realqa/questions/%s/' % q_id)

def downvote(request, q_id, id):

    headers = {
           'Content-Type': 'application/json',
           'Authorization': 'Basic ' + request.session['auth']
           }
		   
    url = "http://realqa.mathcs.emory.edu/nodes/" + str(id) + "/vote?vote_type=down" 

    req = urllib2.Request(url, "", headers)
    
    result = urllib2.urlopen(req)
    return HttpResponseRedirect('/realqa/questions/%s/' % q_id)

    

def login(request):
    template_name = 'realqa/login.html'
    model = User

    # Login user and store API token session
    if request.method == 'POST':
        #TODO: validate, but not really

        # get request data
        username = request.POST['username']
        # password = hashlib.md5(request.POST['password']).hexdigest()
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


# Get questions by tag name
def questionsByTag(request, tag):

    template_name = 'realqa/index.html'

    # if user is logged in
    if 'apiToken' in request.session:
        # request list of questions from API
        req = urllib2.Request('http://realqa.mathcs.emory.edu/questions/?tag_name=%s' % tag)
        results = json.loads(json.dumps(json.load(urllib2.urlopen(req))))

        i = 0
        for str in results['results']:
            taglist = str['tagnames'].split()
            results['results'][i]['tagnames'] = taglist
            i += 1

        context = {'question_list': results}

        return render(request, template_name, context)
    else:
        return HttpResponseRedirect('/realqa/login')

# Register a user
def register(request):

    template_name = 'realqa/register.html'

    if request.method == 'GET':
        # if user has a stored session var, then no need to register
        if 'apiToken' in request.session:
                return render_to_response('realqa/index.html', {'apiToken': request.session['apiToken']})

        return render(request, template_name)

    elif request.method == 'POST':

        username = request.POST['username']
        password = hashlib.md5(request.POST['password']).hexdigest()

        data = {
            "username": username,
            "password": password,
            "device_id": randint(0, 1000)
        }

        data = json.dumps(data)
        headers = {
            "Content-Type": "application/json"
        }

        url = "http://realqa.mathcs.emory.edu/users/"
        req = urllib2.Request(url, data, headers)

        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError, e:
            # For some reason this returns a 500 error, but we should log in user here
            return HttpResponseRedirect('/realqa/login')

        else:
            return HttpResponseRedirect('/realqa/login')