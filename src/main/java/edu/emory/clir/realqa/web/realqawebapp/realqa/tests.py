#import datetime
#from django.utils import timezone
import os
from realqawebapp import settings
from django.test import TestCase
from django.test import Client
from realqa.models import Question
from realqa import views
from django.test.client import RequestFactory #allows use of dummy requests
from django.http import HttpResponseRedirect
from django.db import models


#------------------------------------------------------- ----------------------------------------#
List1 = ['django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'realqa',]

traverseUnit = 0

List2 = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

traverseUnit2 = 0



class Client_Test(TestCase):


#---------------------------------------------------------------------------------------------------#
    def test_checksizeOfApps(self):
            self.assertNotEqual(len(settings.INSTALLED_APPS),0)

#----------------------------------------------------------------------------------------------------#            

    def test_tupleObjectsMatchMIDDLEWARE(self):

        for each in range(0, len(List2)):
        
            foundMatch = False

            traverseUnit = 0
        
            for i in range(0, len(settings.MIDDLEWARE_CLASSES)):
            
                if List2[each] == settings.MIDDLEWARE_CLASSES[traverseUnit]:
            
                    foundMatch = True
                
                traverseUnit += 1

            self.assertEqual(foundMatch, True) #fails, cannot find why

#-------------------------------------------------------------------------------------------------------#

    def test_tupleObjectsMatchINSTALLED_APPS(self):
        
        for each in range(0, len(List1)):
        
            foundMatch = False

            traverseUnit = 0
        
            for i in range(0, len(settings.INSTALLED_APPS)):
            
                if List1[each] == settings.INSTALLED_APPS[traverseUnit]:
            
                    foundMatch = True
                
                traverseUnit += 1

            self.assertEqual(foundMatch, True)


#--------------------------------------------------------------------------------------------------------#
    
    def test_WelcomeToQA(self):
        response = self.client.get('/realqa/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Dashboard', response.content.decode('utf-8')) #fails, needs solution


#----------------------------------------------------------------------------------------------------------#

    def test_loginPage(self):
        response = self.client.get('/realqa/login')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to QA!', response.content.decode('utf-8'))


#----------------------------------------------------------------------------------------------------------#
    def test_inboxPage(self):
        response = self.client.get('/realqa/inbox')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Inbox', response.content.decode('utf-8'))

#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
    def test_profilePage(self):
        response = self.client.get('/realqa/profile')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Your Questions and Answers', response.content.decode('utf-8'))

#----------------------------------------------------------------------------------------------------------#
    def test_yourQuestionsPage(self):
        response = self.client.get('/realqa/5')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Your Questions', response.content.decode('utf-8')) #fails because 'Dashboard' is set to everything

#----------------------------------------------------------------------------------------------------------#
    def test_yourSubscribedQsPage(self):
        response = self.client.get('/realqa/6')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Your Subscribed Questions', response.content.decode('utf-8')) #fails because 'Dashboard' is set to everything

#----------------------------------------------------------------------------------------------------------#
    def test_yourAnsweredQsPage(self):
        response = self.client.get('/realqa/7')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Questions You Answered', response.content.decode('utf-8')) #fails because 'Dashboard' is set to everything

#----------------------------------------------------------------------------------------------------------#

    def test_login(self): #not sure if this is the exact way to make tests of this kind. results can be either pass or fail

        #response = self.client.get('/realqa/login')

        self.factory = RequestFactory()  #dummy request according to tutorial

        request1 = self.factory.get('/realqa/login')

        response = HttpResponseRedirect('/realqa/')

        self.assertEquals(views.login(request1), response)


        #'WSGI Request' object has no attribute 'session'

#----------------------------------------------------------------------------------------------------------#

    def test_post(self):

        self.factory = RequestFactory() #dummy request according to tutorial

        request2 = self.factory.get('/realqa/')

        response = HttpResponseRedirect('/realqa/')

        self.assertEquals(views.askQuestion(request2), response)
        #response = self.client.post('/realqa/', {''})

        #received = json.loads(response.content.decode('utf-8'))
        #self.assertIn('a', received)

        #doesnt post if there is no '#' need to find a way to include this in testing
#----------------------------------------------------------------------------------------------------------#

    def test_post(self):

        self.factory = RequestFactory() #dummy request according to tutorial

        request2 = self.factory.get('/realqa/')
        request2.post['username'] = 'JohnDoe1'
        request2.post['password'] = 'JohnDoe2'

#----------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------#
