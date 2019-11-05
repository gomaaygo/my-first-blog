from django.test import TestCase
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.urls import reverse


class HomePage(TestCase):
    """Classe de testes para a página inicial."""

    def setUp(self):
        """
        Inicializando uma requisição.
        """
        self.resp = self.client.get('')

    def test_home_page(self):
        """
        Verifica se a página inicial está funcionando.
        """
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """
        Verifica se o template que está sendo renderizado é o mesmo.
        """
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')


class PageNewPost(TestCase):
    """
    Classe de teste para a página de novas postagens.
    """

    def setUp(self):
        """Inicializando uma requisição."""
        self.resp = self.client.get('/post/new')

    def test_page(self):
        """
        Verifica se a página com um formulário do novo
        post está funcionando.
        """
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """
        Verifica se o template que está sendo renderizado é o mesmo.
        """
        self.assertTemplateUsed(self.resp, 'blog/post_edit.html')

    def test_add_form(self):
        """
        Verifica se o formulário renderizado é o mesmo da instância.
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, PostForm)

    def test_form(self):
        """
        Verifica a quantidade de elementos do formulário.
        """
        tags = (
            ('<form', 1),
            ('<input', 2),
            ('<submit', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, count)


class PagePostDetail(TestCase):
    """
    Classe de testes para a página onde possui todo o conteúdo
    uma postagem.
    """

    def setUp(self):
        """
        Criando e inicializando objetos necessários para testar.
        """
        user = User(email='msg@gmail.com', username='msg',
                    password='msg123456')
        user.save()

        post = Post(title='Título', text='Conteúdo', author=user)
        post.save()

        '''
        Fazendo uma requisição a página post_detail e enviando os
        argumentos necessários.
        '''
        self.resp = self.client.get(
            reverse('post_detail', kwargs={'pk': post.pk}))

    def test_page(self):
        """
        Verifica se a página post_detail está funcionando.
        """
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """
        Verifica se o template que está sendo renderizado é o mesmo.
        """
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')


class PageEditPost(TestCase):
    """
    Classe de testes para a página onde possui todo o conteúdo
    necessário para editar uma postagem.
    """

    def setUp(self):
        """Criando e inicializando objetos necessários para testar."""
        user = User(email='msg@gmail.com', username='msg',
                    password='msg123456')
        user.save()

        post = Post(title='Título', text='Conteúdo', author=user)
        post.save()

        self.resp = self.client.get(
            reverse('post_edit', kwargs={'pk': post.pk}))

    def test_page(self):
        """
        Verifica se a página que contém o formulário
        para editar post está funcionando.
        """
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        """
        Verifica se o template que está sendo renderizado é o mesmo.
        """
        self.assertTemplateUsed(self.resp, 'blog/post_edit.html')

    def test_add_form(self):
        """
        Verifica se o formulário renderizado é o mesmo da instância.
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, PostForm)

    def test_form(self):
        """
        Verifica a quantidade de elementos do formulário.
        """
        tags = (
            ('<form', 1),
            ('<input', 2),
            ('<submit', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, count)
