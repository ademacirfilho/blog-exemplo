from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('new_post/', views.new_post, name='new_post'),
    path('new_post/<int:post_id>/editar/', 
         views.editar_post, 
         name='editar_post'),
    path('new_post/<int:post_id>/deletar/', 
         views.deletar_post, 
         name='deletar_post'),
    path('contact/', views.contact, name='contact'),
    path('message/', views.message, name='message'),
    path('message/<int:mensagem_id>/editar/', 
         views.editar_mensagem, 
         name='editar_mensagem'),
    path('message/<int:mensagem_id>/deletar/', 
         views.deletar_mensagem, 
         name='deletar_mensagem'),
    path('register/', views.register, name='register')
]