from django.shortcuts import render
from .models import Blog


def allBlogs(request):
    posts = Blog.objects
    return render(request, 'blog/index.html', {"posts": posts})
