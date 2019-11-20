from .models import Post
from .forms import PostForm, PassForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.utils.crypto import get_random_string
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {'posts': posts, 'acao':
                                                   'Postagens'})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form, 'acao':
                                                   'Adicionar'})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form, 'acao':
                                                   'Editar'})


def page_login(request):
    return render(request, 'blog/login.html', {})


def login_views(request):
    username = request.POST['user']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'blog/perfil.html')

    else:
        return render(request, 'blog/login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'blog/login.html', {})


def esqueci_senha(request):
    form = PassForm()
    return render(request, 'blog/esqueci_senha.html', {'form': form})


def senha():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(10, chars)


def go_send(request):
    password = senha()
    subject = 'Olá - Está é uma menssagem da sua app django'
    message = ' Sua nova senha: ' + password
    email_from = request.POST['email']
    username = request.POST['username']
    user = get_object_or_404(User, username=username)
    user.set_password(password)
    user.save()
    recipient_list = ['maiurygarcia@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    msg = 'Seu email foi enviado com sucesso.'
    return render(request, 'blog/esqueci_senha.html', {'msg': msg})
