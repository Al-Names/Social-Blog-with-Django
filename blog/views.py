from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Pearl',
        'title' : 'Blog Post',
        'content': 'Post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Judith',
        'title': 'Blog Post',
        'content': 'Post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': '`linda',
        'title': 'Blog Post',
        'content': 'Post content',
        'date_posted': 'August 27, 2019'
    },

]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About' })


def contact(request):
    return render(request, 'blog/contact.html')

