from django.shortcuts import render
from django.contrib import messages
# Create your views here.r

def message_view(request):

    messages.debug(request,"this is debug message")
    messages.info(request,"this is info message")
    messages.success(request,"this is success message")
    messages.error(request,"this is Error message")
    messages.warning(request,"this is warning message")
    
   
    return render(request,"message.html")
