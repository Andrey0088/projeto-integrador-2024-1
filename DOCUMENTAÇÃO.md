# Documentação

# Guia para Contribuir com o Projeto
Este guia destina-se a desenvolvedores interessados em contribuir com o projeto. Aqui estão algumas diretrizes e instruções para facilitar sua colaboração.

## Como Contribuir

**Crie um ambiente virtual**

 ```shell
    python -m venv nome_do_venv
    .\nome_do_venv\Scripts\activate
```
**Baixe os pacotes para o funcionamento do codigo**
```shell
    pip install django
    pip install pillow
    pip install genai
    pip install google-generativeai #para fins de testes minha CHAVE API aberta.
```

**Faça um clone da aplicação**

```shell
    git clone https://github.com/AlanBMC/projeto-integrador-2024-1-CARDY.git](https://github.com/Andrey0088/projeto-integrador-2024-1.git
    git checkout -b nome-da-sua-branch
    git add .
    git commit -m "Alterações"
    git remote add upstream https://github.com/AlanBMC/projeto-integrador-2024-1-CARDY.git](https://github.com/Andrey0088/projeto-integrador-2024-1.git
    git push origin nome-da-branch
 ```
# DATABASE

Usei o database padrão*

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

# Funções
 Todas as funções tem uma docstring para facilidar o uso dos proximos desenvolvedores.
```python
def cadastro(request):
def home2(request):
def login(request):
def Deslogar(request):
def cadastroSucesso(request):
def Feed(request):
def graficos(request):
def publicate(request):
def nova_disciplina(request):
def filtrar_disciplina(request, nome_disciplina):
def exibir_respostas(request, post_id):
def enviar_resposta(request, post_id):
def delete_post(request, post_id):
def delete_comment(request, comment_id):
def perfil(request, user_id):
def editar_perfil(request, user_id):
```

<h3>Diagrama Entidade Relacional (DER)</h3>
<img src="DER.jpg" width="1000px" style="border-radius: 50%;">

# GUIA BASICO DE NAVEGAÇÃO - desenvolvedor
```python
   from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    # Página principal com feed de posts
    path('feed2/', views.home2, name='feed2'),

    # Autenticação e gerenciamento de usuários
    path('cadastro/', views.cadastro, name='cadastro'),  # Cadastro de novos usuários
    path('login/', views.login, name='login'),  # Login de usuários
    path('cadastro/sucesso/', views.cadastroSucesso, name='cadastroSucesso'),  # Página de sucesso no cadastro
    path('logout/', views.Deslogar, name='logout'),  # Logout de usuários

    # Publicação e gestão de conteúdo
    path('publicate/', views.publicate, name='publicate'),  # Página para publicação de novos posts
    path('nova_disciplina/', views.nova_disciplina, name='nova_disciplina'),  # Adição de novas disciplinas
    path('disciplina/<str:nome_disciplina>/', views.filtrar_disciplina, name='filtrar_disciplina'),  # Filtro de posts por disciplina

    # Respostas e interações
    path('respostas/<int:post_id>/', views.exibir_respostas, name='exibir_respostas'),  # Visualização de respostas de um post
    path('enviar_resposta/<int:post_id>/', views.enviar_resposta, name='enviar_resposta'),  # Envio de respostas para um post

    # Gerenciamento de posts e comentários
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),  # Deleção de um post
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # Deleção de um comentário

    # Perfis de usuário
    path('perfil/<int:user_id>/', views.perfil, name='perfil'),  # Visualização de perfil de usuário
    path('perfil/editar/<int:user_id>/', views.editar_perfil, name='editar_perfil'),  # Edição de perfil de usuário

    # Análise de dados e estatísticas
    path('graficos/', views.graficos, name='graficos'),  # Visualização de gráficos estatísticos
]
```

## GUIA BASICO DE NAVEGAÇÃO - usuario
*Acessa nossa documentação para usuario* [guia para usuarios](MANUAL.md)
