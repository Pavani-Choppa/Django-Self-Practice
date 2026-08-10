from django.shortcuts import render

# Create your views here.

def blog_c(request):

    student_list = [
        {"title": "Pavi", "class": "B.Tech"},
        {"title": "Pavani", "class": "10th"},
        {"title": "Pavvu", "class": "Diploma"},
    ]

    return render(request, "blog.html", {
        "student_list": student_list
    })