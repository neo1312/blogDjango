from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts=Post.published.all()
    context={'posts':posts}
    return render(request,
            'blog/post/list.html',context
            )
