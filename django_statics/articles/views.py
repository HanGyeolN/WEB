from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles':article
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        article = Article(
            title=title,
            image=image,
            content=content
        )
        article.save()
        return redirect("articles:index")
    else:
        return render(request, 'articles/create.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)    
    context = {
        'article' : article
    }
    return render(request, "articles/detail.html", context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }

    if request.method == "POST":
        article.title = request.POST.get("title") or article.title
        article.content = request.POST.get("content") or article.content
        article.image = request.FILES.get("image") or article.image
        article.save()

        return redirect("articles:detail", article.pk)
    
    else:
        return render(request, 'articles/update.html', context)

def delete(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.image.delete()
        article.delete()
        return redirect("articles:index")
    else:
        return redirect("articles:index")
