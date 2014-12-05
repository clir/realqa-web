from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from realqa import views

urlpatterns = patterns('',
    url(r'^$', views.allQuestions, name='index'),
    url(r'^(?P<q_id>\d+)/$', views.questionDetail, name='detail'),
    url(r'^ans/(?P<q_id>\d+)/$', views.answerQuestion, name='ans'),
	url(r'^ask/$', views.askQuestion, name = 'ask'),
	#url(r'^(?P<sort>\d+)/$', views.allQuestionsSort, name='sort'),
	url(r'^count$', views.allQuestionsSortAnsCount, name='sort'),

    url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),

	url(r'^help$', TemplateView.as_view(template_name='realqa/help.html'), name='help'),
	url(r'^register$', TemplateView.as_view(template_name='realqa/register.html'), name='register'),
	url(r'^inbox$', TemplateView.as_view(template_name='realqa/inbox.html'), name='inbox'),
	url(r'^profile$', TemplateView.as_view(template_name='realqa/settings.html'), name='profile'),
    )