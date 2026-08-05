from django.shortcuts import render
from datetime import datetime
# Create your views here.

def blog_details(request):
    post = {
        "title": "My First Blog Post",
        "description": "This is the content of my first blog post.",
        "author": None,
        "created_at": datetime(2026,8,5,22,36),
        "comments_count":6,
        "tags": ["django", "blog", "tutorial","Editing"],
        "price" : 100,
        "number" : 11,
    }
    return render(request, 'blog/index.html', {'post': post})

