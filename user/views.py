from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib import messages
from user.forms import AvatarForm, UserEditForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from user.models import Avatar
import os
from PIL import Image



# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:Login")
        else:
            return render(request, "user/register.html", {"form": form, "errors": form.errors})
    form = UserRegisterForm()
    return render(request, "user/register.html", {"form": form})

# ----------------------------------------------------------------------------------------------------


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home:Index")

        return render(request, "user/login.html", {'form': form})

    form = AuthenticationForm()
    return render(request, "user/login.html", {'form': form})

# ----------------------------------------------------------------------------------------------------


def logout_request(request):
    logout(request)
    return redirect("user:Login")

# ----------------------------------------------------------------------------------------------------


@login_required
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home:Index')
    

    form = UserEditForm(model_to_dict(user))
    avatares = Avatar.objects.filter(user=user.id)
    print("AVATARES",len(avatares))
    if len(avatares) == 0:
      url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/271deea8-e28c-41a3-aaf5-2913f5f48be6/de7834s-6515bd40-8b2c-4dc6-a843-5ac1a95a8b55.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI3MWRlZWE4LWUyOGMtNDFhMy1hYWY1LTI5MTNmNWY0OGJlNlwvZGU3ODM0cy02NTE1YmQ0MC04YjJjLTRkYzYtYTg0My01YWMxYTk1YThiNTUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.BopkDn1ptIwbmcKHdAOlYHyAOOACXW0Zfgbs0-6BY-E"
    else:
      url = avatares[0].image.url
    return render(request, "user/profile.html", {'form': form, "url": url})

# ----------------------------------------------------------------------------------------------------

@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            return redirect('home:Index')

    form= AvatarForm()
    return render(request, "user/avatar.html",{"form": form})