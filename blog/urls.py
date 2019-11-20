from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('page/login', views.page_login, name='page_login'),
    path('login_views', views.login_views, name='login_views'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('esqueci_senha', views.esqueci_senha, name='esqueci_senha'),
    path('go_send', views.go_send, name='go_send'),
]
