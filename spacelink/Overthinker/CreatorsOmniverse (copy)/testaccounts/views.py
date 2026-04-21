from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .forms.auth_forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")  # Redirect to root homepage after register
    else:
        form = RegisterForm()
    return render(request, "testaccounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("/")  # Redirect to root homepage after login
    else:
        form = LoginForm()
    return render(request, "testaccounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("testaccounts:login")


# Removed profile_view since it's no longer needed
