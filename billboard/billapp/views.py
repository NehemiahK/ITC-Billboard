# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Post
from .forms import PostForm 

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
    return render(request, 'billapp/page1.html', {'post_list': posts, 'form':form})
