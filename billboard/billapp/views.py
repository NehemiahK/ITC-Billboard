# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm


from .models import Post
from .forms import PostForm, UserForm

from django.http import HttpResponse

def new_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # check form validity
            post = form.save(commit=False)
            #post.published_date = timezone.now()
            post.save() # save the post
            return redirect('index') # run the index method to go back to main page
    else:
        form = PostForm()
    return render(request, 'billapp/page1.html', {'form': form})


def index(request):
    form = PostForm() # the form to fillout a post
    posts = Post.objects.all() # return all posts from the models.py --> post
    # return the form and the posts to send over to the html file

    return render(request, 'billapp/page1.html', {'post_list': posts, 'form':form, 'user':request.user})

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            auth = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            login(request, auth)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')
