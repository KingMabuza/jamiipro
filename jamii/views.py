from django.shortcuts import render
from newsapi import NewsApiClient
from .models import Post


def index(request):
    newsapi = NewsApiClient(api_key="922bccdaca334a0daa16d903ff1b8e26")
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

    obj = Post.objects.get(id=2)
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
    return render(request, 'jamii/blog.html')


def contact(request):
    return render(request, 'jamii/contact.html')


def events(request):
    return render(request, 'jamii/events.html')


def explorer(request):
    return render(request, 'jamii/explorer.html')


def glossary(request):
    return render(request, 'jamii/glossary.html')


def login(request):
    return render(request, 'jamii/login.html')


def news(request):
    return render(request, 'jamii/news.html')


def opportunities(request):
    return render(request, 'jamii/opportunities.html')


def signup(request):
    return render(request, 'jamii/signup.html')


def subscribe(request):
    return render(request, 'jamii/subscribe.html')

