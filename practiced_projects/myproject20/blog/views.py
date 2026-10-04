from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    post =Post.objects.all().order_by('id')
    paginator = Paginator(post, 4)  # Show 4 posts per page
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'post_list.html', {'page_obj': page_obj})