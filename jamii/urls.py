from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog/<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('events', views.events, name='events'),
    path('events/<slug:slug>/', views.EventDetail.as_view(), name='event_detail'),
    path('trade_explorer', views.explorer, name='explorer'),
    path('glossary', views.glossary, name='glossary'),
    path('login', auth_views.LoginView.as_view(template_name='jamii/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='jamii/logout.html'), name='logout'),
    path('news', views.news, name='news'),
    path('opportunities', views.opportunities, name='opportunities'),
    path('signup', views.signup, name='signup'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('profile', views.profile, name='profile'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='jamii/password_reset.html'),
         name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='jamii/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='jamii/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='jamii/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change', views.PasswordsChangeView.as_view(template_name='jamii/change_password.html'), name='password-change'),
]
