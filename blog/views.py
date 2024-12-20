from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from .models import Post, Blog, Mensagem
from .forms import MensagemForm, PostForm
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first()
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
        "blog": Blog.objects.first()
    }
    return render(request, "post.html", context)

def about(request):
    context = {
        "blog": Blog.objects.first()
    }
    return render(request, "about.html", context)

@login_required
def new_post(request):
    context = {
        "blog": Blog.objects.first(),
    }

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context["form"] = form
    else:
        context["form"] = PostForm()

    return render(request, "new_post.html", context)

def editar_post(request, post_id):
    poste = get_object_or_404(Post, pk=post_id)
    context = {
        "blog": Blog.objects.first(),
        "form": PostForm(instance=poste)
    }

    if request.method == "POST":
        form = PostForm(request.POST, instance=poste)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context["form"] = form

    return render (request, "new_post.html", context)

def deletar_post(request, post_id):
    context = {
        "blog": Blog.objects.first(),
        "post" : get_object_or_404(Post, pk=post_id)
    }

    if request.method == 'POST':
        context["mensagem"].delete()
        return redirect('index')
    else:
        return render (request, "delete_post.html", context)

def contact(request):
    context = {
        "blog": Blog.objects.first(),
    }

    if request.method == "POST":
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
        else:
            context["form"] = form
    else:
        context["form"] = MensagemForm()
       
    return render(request, "contact.html", context)
    
def message(request):
    context = {
        "mensagens" : Mensagem.objects.all()
    }

    return render (request, "message.html", context)

def editar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    context = {
        "blog": Blog.objects.first(),
        "form": MensagemForm(instance=mensagem)
    }

    if request.method == "POST":
        form = MensagemForm(request.POST, instance=mensagem)
        if form.is_valid():
            form.save()
            return redirect('message')
        else:
            context["form"] = form

    return render (request, "contact.html", context)

def deletar_mensagem (request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem" : get_object_or_404(Mensagem, pk=mensagem_id)
    }

    if request.method == 'POST':
        context["mensagem"].delete()
        return redirect('message')
    else:
        return render (request, "delete_contact.html", context)
    
def register(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "register.html", context)