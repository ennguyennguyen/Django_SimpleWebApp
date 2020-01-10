from django.http import HttpResponse #library to send response back to users

def about(request):
    return HttpResponse('About')

def home(request):
    return HttpResponse('Homepage')