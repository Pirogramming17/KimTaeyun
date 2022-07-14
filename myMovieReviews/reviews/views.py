from django.shortcuts import render, redirect
from .models import Review

def home(request):
    reviews = Review.objects.all()

    context = {
        "reviews":reviews
    }
    return render(request, template_name="reviews/home.html", context=context)


def create(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST["title"]
        release_yr = request.POST["release_yr"]
        genre = request.POST["genre"]
        rating = request.POST["rating"]
        running_time = request.POST["running_time"]
        content = request.POST["content"]
        director = request.POST["director"]
        actors = request.POST["actors"]

        Review.objects.create(title= title, release_yr=release_yr, genre=genre, rating=rating, running_time=running_time, content=content, director=director, actors=actors)
        
        return redirect("/")

    context = {}

    return render(request, template_name="reviews/create.html", context=context)

def detail(request, id):
    review = Review.objects.get(id=id)
    context = {
        "review": review
    }
    return render(request, template_name="reviews/detail.html", context=context)

def update(request, id):
        if request.method == "POST":
            title = request.POST["title"]
            release_yr = request.POST["release_yr"]
            genre = request.POST["genre"]
            rating = request.POST["rating"]
            running_time = request.POST["running_time"]
            content = request.POST["content"]
            director = request.POST["director"]
            actors = request.POST["actors"]

            Review.objects.filter(id=id).update(title= title, release_yr=release_yr, genre=genre, rating=rating, running_time=running_time, content=content, director=director, actors=actors)

            return redirect(f"/review/{id}")
    
        elif request.method == "GET":
            review = Review.objects.get(id=id)
            context = {
                "review":review
            }
            return render(request, template_name="reviews/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Review.objects.filter(id=id).delete()
        return redirect("/")