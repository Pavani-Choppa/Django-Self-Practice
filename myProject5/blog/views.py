from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def home(request):
    context = {
            "name" : "Pavani Choppa",
            "age" : 22,
            "skills" : ["Python", "Django", "Editing"],
            "user" : User("Pavani", 22),
            "blog" : {
                "title" : "My First Blog",
                "content" : "<b> This is my first blog post. I am excited to share my thoughts and experiences with you all. Stay tuned for more updates! </b>",
                "date_posted" : datetime(2026, 8, 4, 11, 33),
                "author" : {
                    "name" : "Pavani Choppa",
                    "age" : 22,
                    "email" : "pavani.choppa@example.com"
                }
            },
            "empty_value" : None,
    }
    return render(request, "blog/home.html",context)

    
