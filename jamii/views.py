from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from newsapi import NewsApiClient
from .models import Post
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .models import Post

newsapi = NewsApiClient(api_key="922bccdaca334a0daa16d903ff1b8e26")


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
    }

    return render(request, 'jamii/home.html', context={"mylist": mylist, "blog_post": blog_post})


def about(request):
    return render(request, 'jamii/about.html')


def blog(request):
    posts = Post.objects.all()
    return render(request, 'jamii/blog.html', {'posts': posts})


def contact(request):
    return render(request, 'jamii/contact.html')


@login_required
def events(request):
    return render(request, 'jamii/events.html')


@login_required
def explorer(request):
    return render(request, 'jamii/explorer.html')


def glossary(request):
    return render(request, 'jamii/glossary.html')


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
