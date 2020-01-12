from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# [NGUYEN] this is the file to control what the viewer will see when accessing the Article page

# Create your views here.
def article_list(request):
    
    # grab all article objects from database
    articles = Article.objects.all().order_by('date')

    # update to display articles objects using a dictionary {'articles': articles}
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_details(request, slug):
    return HttpResponse(slug)