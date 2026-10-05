from django.shortcuts import render
from .models import Post
from django.db.models import Q
# Create your views here.


def post_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )
    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'query': query, 'category': category})