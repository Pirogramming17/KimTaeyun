from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, template_name="posts/home.html", context=context)

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        description = request.POST["description"]
        interest = request.POST["interest"]
        expected_tool = request.POST["expected_tool"]

        Post.objects.create(title= title, photo=req_photo, description=description, interest=interest, expected_tool=expected_tool)
        
        return redirect("/")

    context = {}

    return render(request, template_name="posts/create.html", context=context)


def detail(request, id):
    posts = Post.objects.get(id=id)
    context = {
    }
    return render(request, template_name="posts/detail.html", context=context)


def update(request, id):
    if request.method == "POST":
        title = request.POST["title"]
        req_photo = request.FILES["photo"]
        description = request.POST["description"]
        interest = request.POST["interest"]
        expected_tool = request.POST["expected_tool"]

        Post.objects.filter(id=id).update(title= title, photo=req_photo, description=description, interest=interest, expected_tool=expected_tool)
        return redirect(f"/post/{id}")
    
    elif request.method == "GET":
        post = Post.objects.get(id=id)
        context = {
            "post": post
        }
        return render(request, template_name="posts/update.html", context=context)

def delete(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return redirect("/")


