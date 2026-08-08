from datetime import datetime

from django.shortcuts import render

# Create your views here.

def blog_list(request):
    blogs = [
        {"title":"Go For It","is_featured":True,"Author":"Ashok Naik"},
        {"title":"Editing","is_featured":False,"Author":"Pavani"},
        {"title":"Thumbnail","is_featured":True,"Author":""},
        {"title":"Boy Frienship","is_featured":True,"Author":"Lavs"},
        {"title":"Family & Friends","is_featured":True,"Author":"Gayathri"},
    ]
    context = {
        "blog": blogs,
        "today": datetime.now(),
        "html_code": "<h1> Welcome to My Blog </h1>"
    }
    return render(request, 'blog/blog_details.html',context)
