from . import views
from django.contrib import admin
from django.urls import include, path

app_name = 'auth'


urlpatterns = [    
    path('feed2/', views.home2, name='feed2'),    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('cadastro/sucesso/', views.cadastroSucesso, name='cadastroSucesso'),
    path('publicate/', views.publicate, name='publicate'),
    path('nova_disciplina/', views.nova_disciplina, name='nova_disciplina'),
    path('disciplina/<str:nome_disciplina>/', views.filtrar_disciplina, name='filtrar_disciplina'),
    path('logout/', views.Deslogar, name='logout'),
    path('respostas/<int:post_id>/', views.exibir_respostas, name='exibir_respostas'),
    path('enviar_resposta/<int:post_id>/', views.enviar_resposta, name='enviar_resposta'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('perfil/<int:user_id>/', views.perfil, name='perfil'),
    path('perfil/editar/<int:user_id>/', views.editar_perfil, name='editar_perfil'),
    path('graficos', views.graficos, name="graficos")
]
