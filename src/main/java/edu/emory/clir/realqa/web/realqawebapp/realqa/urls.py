from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from realqa import views

urlpatterns = patterns('', 
    url(r'^login$', TemplateView.as_view(template_name='realqa/login.html'), name='login'),
	url(r'^logout$', TemplateView.as_view(template_name='realqa/logout.html'), name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^help$', TemplateView.as_view(template_name='realqa/help.html'), name='help'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^register$', TemplateView.as_view(template_name='realqa/register.html'), name='register'),
	url(r'^inbox$', TemplateView.as_view(template_name='realqa/inbox.html'), name='inbox'),
	url(r'^profile$', TemplateView.as_view(template_name='realqa/settings.html'), name='profile'),
    )