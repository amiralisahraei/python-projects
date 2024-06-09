from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseBadRequest
from . import models
from .forms import MemberForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm


def home(request):
    return render(request, "index.html")


def members(request):
    member = models.Member.objects.all().values()
    context = {"myusers": member}
    return render(request, "all_members.html", context)


def details(request, slug):
    member = models.Member.objects.get(slug=slug)
    context = {"myuser": member}
    return render(request, "details.html", context)


def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New member has been created.")
            return redirect("/members")
    else:
        form = MemberForm()

    return render(request, "add_member.html", {"form": form})


def update_member(request, slug):
    member = get_object_or_404(models.Member, slug=slug)
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Memeber {member.firstname} {member.lastname} has been updated",
            )
            return redirect("/members")
    else:
        form = MemberForm(instance=member)

    return render(request, "update_member.html", {"form": form})


def delete_member(request, slug):
    member = get_object_or_404(models.Member, slug=slug)
    if request.method == "POST":
        member.delete()
        messages.success(
            request, f"Member {member.firstname} {member.lastname} has been deleted."
        )
        return redirect("/members")

    else:
        HttpResponseBadRequest("Invalid Request!")


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password :(")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")
