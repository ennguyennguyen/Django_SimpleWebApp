from django.http import HttpResponse # library to send response back to users
from django.shortcuts import render # library to render the html pages

def about(request):
    #return HttpResponse('About')
    return render(request, 'about.html')

def home(request):
    #return HttpResponse('Homepage')
    return render(request, 'homepage.html')