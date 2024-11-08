from django.shortcuts import render
from .models import Post, Blog, Mensagem

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

def contact(request):
    context = {
        "blog": Blog.objects.first(),
    }

    if request.method == "POST":
        context['erro'] = {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['mensagem']:
            context['erro']['mensagem'] = True

        if context ['erro']:
            return render(request, "contact.html", context)

        mensagem = Mensagem(nome = request.POST['nome'],
                            email = request.POST['email'],
                            telefone = request.POST['telefone'],
                            cidade = request.POST['cidade'],
                            mensagem = request.POST['mensagem'])
        
        mensagem.save()

        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)
    
def message(request):
    context = {
        "mensagens" : Mensagem.objects.all()
    }

    return render (request, "message.html", context)