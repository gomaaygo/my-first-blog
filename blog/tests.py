from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class HomePage(TestCase):
    """Classe de testes para a página inicial."""

    def setUp(self):
        """Inicializando..."""
        self.resp = self.client.get('')

    def test_home_page(self):
        """Verifica se a página inicial está funcionando."""
        self.assertEqual(self.resp.status_code, 200)


class PageNewPost(TestCase):
    """Classe de teste para a página de novas postagens."""

    def setUp(self):
        """Inicializando..."""
        self.resp = self.client.get('/post/new')

    def test_form_new_post(self):
        """Verifica se a página com um formulário do novo
        post está funcionando"""
        self.assertEqual(self.resp.status_code, 200)


class PagePostDetail(TestCase):
    """Classe de testes para a página onde possui todo o conteúdo
    uma postagem"""

    def setUp(self):
        """Criando e inicializando objetos necessários para testar."""
        user = User(email='msg@gmail.com', username='msg',
                    password='msg123456')
        user.save()

        post = Post(title='Título', text='Conteúdo', author=user)
        post.save()

        self.resp = self.client.get('post/post.pk/')

    def test_page_post_detail(self):
        """Verifica se a página inicial está funcionando"""
        self.assertEqual(self.resp.status_code, 200)


'''class PageEditPost(TestCase):
    post = get_object_or_404(Post, pk=pk)

    def setUp(self):
        self.resp = self.client.get('/post/post.pk/edit')

    def test_form_edit_postt(self):
        """Verifica se a página que contém o formulário
        para editar post está funcioando."""
        self.assertEqual(self.resp.status_code, 200)
        # self.assertEqual(self.resp.status_code, 200)'''


'''class FormNewPost(TestCase):
    def setUp(self):
        self.resp = self.client.get('/post/new')

    def test_html(self):
        tags = (
            ('<form', 1),
            ('<input', 1),
            ('<submit', 1)
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)'''
