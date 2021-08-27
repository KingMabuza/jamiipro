from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from newsapi import NewsApiClient
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm, ExportRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .models import Exporter, Post, Glossary, About
from django.core.mail import send_mail
from django.conf import settings

newsapi = NewsApiClient(api_key="de8d7936b3ea407a896b753b35430fa3")


def index(request):
    all_articles = newsapi.get_everything(q='afcfta',
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=3)

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    url = []
    author = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        author.append(myarticles['author'])
    mylist = zip(news, desc, img, url, author)

    obj = Post.objects.get(id=1)
    blog_post = {
        'title': obj.title,
        'cover': obj.cover,
        'description': obj.description,
        'date': obj.date_posted,
        'body': obj.body,
        'slug': obj.slug
    }

    return render(request, 'jamii/home.html', context={"mylist": mylist, "blog_post": blog_post})


def about(request):
    abouts = About.objects.all()
    return render(request, 'jamii/about.html', {'abouts': abouts})


def blog(request):
    posts = Post.objects.all()
    return render(request, 'jamii/blog.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':

        notification = 'Thank you for your email, we will get back to you shortly'

        name = request.POST.get('name')
        email_sender = request.POST.get('email_sender')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject=subject,
            message=f"NAME: {name} \n \n EMAIL ADDRESS: {email_sender} \n \n MESSAGE: {message}",
            from_email=email_sender,
            recipient_list=['afcftajamii@gmail.com']
        )
        return render(request, 'jamii/contact.html', {'notification': notification})
    else:
        return render(request, 'jamii/contact.html')


@login_required
def events(request):
    return render(request, 'jamii/events.html')


@login_required
def explorer(request):
    Exporter_Objs = Exporter.objects.all().last()
    if request.method == 'POST':
        form = ExportRegisterForm(request.POST)
        #user = User.objects.get(username=request.user.username)
        if form.is_valid(): 
            Export_Industry = form.cleaned_data.get('Export_Industry')
            Export_From = form.cleaned_data.get('Export_From')
            Export_To = form.cleaned_data.get('Export_To')
            export_obj = Exporter.objects.filter(Export_Industry=Export_Industry, Export_From=Export_From,Export_To=Export_To )
            print("************Our export object************",export_obj)
        return render(request, 'jamii/explorer.html',{'export_obj': export_obj} )
    form = ExportRegisterForm()
    return render(request, 'jamii/explorer.html',{'export_objs': Exporter_Objs, "form":form } )


def glossary(request):
    term = Glossary.objects.all()
    return render(request, 'jamii/glossary.html', {'term': term})


def login(request):
    form = UserCreationForm()
    return render(request, 'jamii/login.html', {'form': form})


def news(request):
    all_articles = newsapi.get_everything(q='afcfta',
                                          language='en',
                                          sort_by='relevancy',
                                          )

    articles = all_articles['articles']

    desc = []
    news = []
    img = []
    url = []
    author = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        author.append(myarticles['author'])
    mylist = zip(news, desc, img, url, author)

    return render(request, 'jamii/news.html', context={"mylist": mylist})


@login_required
def opportunities(request):
    return render(request, 'jamii/opportunities.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted Created Successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'jamii/signup.html', {'form': form})


def subscribe(request):
    return render(request, 'jamii/subscribe.html')


@login_required
def profile(request):
    return render(request, 'jamii/profile.html')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')
