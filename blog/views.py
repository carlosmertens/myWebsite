from django.shortcuts import render, get_object_or_404
from .models import Blog


def allBlogs(request):
    posts = Blog.objects
    return render(request, 'blog/index.html', {"posts": posts})


def theBlog(request, blog_id):
    theblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/theBlog.html', {'theblog': theblog})
