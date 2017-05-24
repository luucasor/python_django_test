# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from core.models import Post
from core.forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def lista(request):
    lista = Post.objects.all().order_by('-id')
    return render(request, 'core/lista.html', {'lista_posts':lista})

def novo(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista)

    return render(request, 'core/novo.html', {'form':form})

def atualiza(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect(lista)

    return render(request, 'core/novo.html', {'form':form})

def deleta(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(lista)
