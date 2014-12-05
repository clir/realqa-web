from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from realqa import views

urlpatterns = patterns('',
    url(r'^$', views.allQuestions, name='index'),

    url(r'^questions/(?P<q_id>\d+)/$', views.questionDetail, name='detail'),
    url(r'^questions/(?P<q_id>\d+)/answer/$', views.answerQuestion, name='ans'),
	url(r'^questions/ask/$', views.askQuestion, name = 'ask'),
    url(r'^questions/tags/(?P<tag>.+)/$', views.questionsByTag, name='tags'),
	url(r'^(?P<sort>\d+)/$', views.allQuestionsSort, name='sort'),


    url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),

	url(r'^help$', TemplateView.as_view(template_name='realqa/help.html'), name='help'),
	url(r'^register$', TemplateView.as_view(template_name='realqa/register.html'), name='register'),
	url(r'^inbox$', TemplateView.as_view(template_name='realqa/inbox.html'), name='inbox'),
	url(r'^profile$', TemplateView.as_view(template_name='realqa/settings.html'), name='profile'),
    )