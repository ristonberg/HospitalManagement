from django.conf.urls import patterns, url

from HMS import views

urlpatterns = patterns('',
    url(r'homepage', views.homepage, name='homepage'),
    url(r'login', views.login, name='login'),
    url(r'registration', views.registration, name='registration')
)
