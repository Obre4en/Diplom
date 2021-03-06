from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import CustomUser
from articles.models import Article
from django.urls import reverse_lazy

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"{username} registration successful")

            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/registration.html", {"form": form})

@login_required
def profile(request):
    articles_by_user = {"articles_by_user": Article.objects.filter(author=request.user)}
    return render(request, "users/profile.html", articles_by_user)

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "changes saved")
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=request.user)

    data = {"form": form}
    return render(request, "users/edit_profile.html", data)
