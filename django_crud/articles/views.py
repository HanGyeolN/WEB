from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        
        'articles': articles,

    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # form으로 넘긴 데이터를 가져오는 방법
    title = request.POST.get("title")
    content = request.POST.get("content")    
    Article.objects.create(title=title, content=content)
    return redirect('/articles/')
