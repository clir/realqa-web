from django.conf.urls import patterns, url
from realqa import views

urlpatterns = patterns('', 
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'realqa/login.html'}),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    )