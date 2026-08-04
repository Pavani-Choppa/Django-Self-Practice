from django.shortcuts import render

# Create your views here.
def app2_fun(request):
    return render(request, 'Template_app2/app2.html')

def app2_html_fun(request):
    return render(request, 'Template_app2/app2_html.html')