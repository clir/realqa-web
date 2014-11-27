from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from realqa import views

urlpatterns = patterns('', 
    url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^register$', views.register, name='register'),
	url(r'^inbox$', TemplateView.as_view(template_name='realqa/inbox.html'), name='inbox'),
	url(r'^profile$', TemplateView.as_view(template_name='realqa/settings.html'), name='profile'),
    )