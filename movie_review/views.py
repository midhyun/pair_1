from django.shortcuts import render, redirect
from .models import Review

def index(request):
    reviews = Review.objects.all()
    # reviews = Review.objects.all()
    
    # context ={
    #     'reviews':reviews,
    # }
    reviews_list = []
    c = 0
    for i in reviews:
        c += 1
        reviews_list.append({'review' : i , 'num': c})
    context = {
        'reviews' : reviews_list ,
    }
    return render(request, 'movie_review/index.html', context)

def new(request):

    return render(request, 'movie_review/new.html')

def create(request):
    content = request.GET.get('content')
    title = request.GET.get('title')
    Review.objects.create(
        content=content,
        title=title
    )
    return redirect('movie_review:index')

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context ={
        'review':review
    }
    return render(request, 'movie_review/detail.html', context)

def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context ={
        'review':review
    }
    return render(request, 'movie_review/edit.html', context)

def modify(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.save()

    return redirect('movie_review:index')

def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()

    return redirect('movie_review:index')