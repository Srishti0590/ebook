from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.auth import user_only
from pickabook.models import Quotes, Category, Books, News


@login_required
@user_only
def homepage(request):
    context = {
        'activate_homepage': 'active'
    }
    return render(request, 'frontend/homepage.html', context)


def show_quotes(request):
    quotes = Quotes.objects.all().order_by('-id')
    context={
        'quotes': quotes,
        'activate_quotes_user': 'active'
    }
    return render(request, 'frontend/show_quotes.html', context)


def show_categories(request):
    categories= Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category': 'active'
    }
    return render(request, 'frontend/show_categories.html', context)


def show_books(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category,
        'activate_book': 'active'
    }
    return render(request, 'frontend/show_books.html', context)


def all_books(request):
    book = Books.objects.all().order_by('-id')
    context = {
        'book': book,
        'activate_book': 'active'
    }
    return render(request, 'frontend/all_books.html', context)


def recommend(request, pk):
    book = Books.objects.get(pk=6)
    context = {
        'book': book,
        'activate_book': 'active'
    }
    return render(request, 'frontend/all_books.html', context)


def book_detail(request, ):
    book = Books.objects.get
    context = {
        'book': book,
        'activate_book_detail': 'active'
    }
    return render(request, 'frontend/book_detail.html', context)


def show_news(request):
    news = News.objects.all().order_by('-id')
    context = {
        'news': news,
        'activate_news': 'active'
    }
    return render(request, 'frontend/show_news.html', context)



