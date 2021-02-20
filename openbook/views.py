from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home_view(request):
    return render(request,"home.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


@csrf_exempt
def donatebook_view(request):
    if request.method == 'POST':

        bookname = request.POST["bookname"]
        author = request.POST["author"]
        b = Book(name=bookname,author=author)
        b.save()
        return render(request,"donatebook.html",{
            "message": "added book"
        })
    else:
        return render(request,"donatebook.html")



def view_book(request):
    books = Book.objects.all()
    return render(request, "allbook.html", {'books': books})