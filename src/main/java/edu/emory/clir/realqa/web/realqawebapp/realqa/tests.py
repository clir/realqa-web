#import datetime
#from django.utils import timezone
import os
from realqawebapp import settings
from django.test import TestCase
from django.test import Client
from realqa.models import Question
from realqa import views
from django.test.client import RequestFactory #allows use of dummy requests


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
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
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

            self.assertEqual(foundMatch, True)

#-------------------------------------------------------------------------------------------------------#

    def test_tupleObjectsMatchINSTALLED_APPS(self):
        
        for each in range(0, len(List1)):
        
            foundMatch = False

            traverseUnit = 0
        
            for i in range(0, len(settings.INSTALLED_APPS)):
            
                if List1[each] == settings.INSTALLED_APPS[traverseUnit]:
            
                    foundMatch = True
                
                traverseUnit += 1

            assert foundMatch == True


#--------------------------------------------------------------------------------------------------------#
    
    def test_WelcomeToQA(self):
        response = self.client.get('/realqa/login')

        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to QA!', response.content.decode('utf-8'))


#----------------------------------------------------------------------------------------------------------#

    def test_login(self):

        #response = self.client.get('/realqa/login')

        self.factory = RequestFactory()

        request1 = self.factory.get('/realqa/login')

        response = HttpResponseRedirect('/realqa/')

        self.assertEquals(views.login(request1), response)


        

#----------------------------------------------------------------------------------------------------------#

    #def test_postHello(self):
        

#----------------------------------------------------------------------------------------------------------#
