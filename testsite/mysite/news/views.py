from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import *
from .forms import *

# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news/home_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Main'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)

def index(request):
    news = News.objects.all()

    context = {
        'news': news,
        'title': 'News List',
    }
    return render(request, 'news/index.html', context)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/index.html', context)

def view_news(request, news_id):
  # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)

    context = {
        'news_item': news_item
    }
    return render(request, 'news/view_news.html', context)

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #news = News.objects.create(**form.cleaned_data)

            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})