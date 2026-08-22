from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from accounts.forms import CustomUserCreationForm,CustomAuthenticationForm
# Create your views here.

# def register(request):
    # if request.method == "POST":

    #     firstname = request.POST.get("firstname")
    #     lastname = request.POST.get("lastname")
    #     username = request.POST.get("username")
    #     password = request.POST.get("password")

    #     if User.objects.filter(username = username).exists():
    #         return render(request,"register.html" ,{"error" :"User name Already Exists"})

    #     User.objects.create_user(
    #         first_name = firstname,
    #         last_name = lastname,
    #         username = username,
    #         password = password
    #     )
    #     return redirect('/login/')
    # return render(request,'register.html')

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             print("FORM IS VALID")
#             form.save()
#             print("USER SAVED")
#             return redirect("login")
#         else:
#             print("FORM IS INVALID")
#             print(form.errors)
            
#     else:
#         print("GET REQUEST RECEIVED")
#         form = UserCreationForm()
#     return render(request, "register.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CustomUserCreationForm()
    return render(request,"register.html",{"form":form})

# def login_page(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(
#             request,
#             username = username,
#             password = password
#         )

#         if user is not None:
#             login(request,user)
#             return redirect('/dashboard/')
        
#         else:
#             return render(request,'login.html',{"error":"Invalid USername or Password correct it"})
   
#     return render(request,'login.html')


def login_page(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            # return redirect("/dashboard/")
            return redirect(request.GET.get("next","/dashboard/"))

    else:
        form = CustomAuthenticationForm()
    return render(request,'login.html',{'from':form})


            
@login_required
def dashboard_page(request):
    print("User : ",request.user)
    print(request.user.is_authenticated)
    print("Session Key : ",request.session.session_key)
    print("Session DAta : ",request.session.items())

    return render(request,'dashboard.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')