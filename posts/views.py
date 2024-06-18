from django.shortcuts import render
from .models import Post

def posts_lists(request):
    posts = Post.objects.all().order_by('-date')

    return render(
        request, 
        "posts/posts_list.html", 
        {'posts': posts}
    )
