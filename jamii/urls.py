from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('trade_explorer', views.explorer, name='explorer'),
    path('glossary', views.glossary, name='glossary'),
    path('login', views.login, name='login'),
    path('news', views.news, name='news'),
    path('opportunities', views.opportunities, name='opportunities'),
    path('signup', views.blog, name='signup'),
    path('subscribe', views.subscribe, name='subscribe'),
]

