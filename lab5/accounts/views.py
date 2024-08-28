from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def login(request):
    form = AuthenticationForm()
    context = {"form": form}
    if request.method == "POST":
        # userobj = User.objects.filter(
        #     username=request.POST["username"], password=request.POST["password"]
        # ).first()
        userobj = authenticate(
            username=request.POST["username"], password=request.POST["password"]
        )
        # if len(userobj) > 0:
        if userobj is not None:
            login(request)
            return redirect(request, "trainee_list")
        else:
            print("invalid username or password")
    return render(request, "accounts/login.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm2(request.POST)
        if form.is_valid():
            # form.save(commit=True)
            User.objects.create_user()
            return render("login")
    else:
        form = UserRegistrationForm2()
        return render(request, "accounts/register.html", {"form": form})
