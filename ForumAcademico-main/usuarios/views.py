from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Post, Respostas, Pessoa,  Disciplina
from django.contrib import messages
from django.db.models import Count

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        qualificacao = request.POST.get('qualificacao')
        semestre = request.POST.get('semestre', None)
        foto_perfil = request.FILES.get('foto_perfil')  
              
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Já existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        user_profile = Pessoa(user=user, foto_perfil=foto_perfil, qualificacao=qualificacao, semestre=semestre)
        user_profile.save()

        
        return redirect('auth:cadastroSucesso')

def home2(request):
    pesquisa = request.GET.get('pesquisa', '')  
    disciplinas = Disciplina.objects.all()  # Obtendo todas as disciplinas
    if pesquisa:
        posts = Post.objects.filter(content__icontains=pesquisa).order_by('-date')  # Filtra por pesquisa
    else:
        posts = Post.objects.all().order_by('-date')  # posts ordenados por data
    context = {
        'posts': posts,
        'disciplinas': disciplinas,  # Passando as disciplinas para o contexto
        'user': request.user
    }
    return render(request, 'feed2.html', context)



def login(request):     
    if request.method == "GET":
        return render(request, 'login.html')    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user is not None:
            login_django(request, user)  
            return redirect('feed')
        
        else:
            messages.error(request, 'Login ou senha inválidos')
            return redirect('auth:login')
        
def Deslogar(request):
    logout(request)
    return redirect('/auth/login')

def cadastroSucesso(request):
    return render(request, 'cadastroSucesso.html')


def Feed(request):
    pesquisa = request.GET.get('pesquisa', '')  
    disciplinas = Disciplina.objects.all()  # Obtém as disciplinas

    if pesquisa:
        posts = Post.objects.filter(content__icontains=pesquisa).order_by('-date')  
    else:
        posts = Post.objects.all().order_by('-date')  
    context = {
        'posts': posts,
        'disciplinas': disciplinas,        

    }
    return render(request, 'feed2.html', context)


def graficos(request):
    # Busca todas as disciplinas e conta o número de posts associados a cada uma
    disciplinas_com_postagens = Disciplina.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')
    
    # Prepara os dados para o gráfico
    dados_grafico = [{'category': disciplina.nome, 'value': disciplina.num_posts} for disciplina in disciplinas_com_postagens]
    
    # Passa os dados e as disciplinas para o template
    context = {
        'dados_grafico': dados_grafico,
        'disciplinas': Disciplina.objects.all(),  # Isso garantirá que a sidebar tenha as disciplinas listadas
    }
    
    return render(request, 'graficos.html', context)




@login_required(login_url="/auth/login/")
def publicate(request):
    if request.method == 'POST':
        content = request.POST.get("content")
        disciplina_ids = request.POST.getlist('disciplinas') 

        post = Post(author=request.user, content=content)
        post.save()  
        
        # Adiciona as disciplinas selecionadas ao post
        for disciplina_id in disciplina_ids:
            disciplina = Disciplina.objects.get(id=disciplina_id)
            post.disciplinas.add(disciplina)
        return redirect('auth:feed2') 
    else:
        disciplinas = Disciplina.objects.all()
        return render(request, 'publicate.html', {'disciplinas': disciplinas})

def nova_disciplina(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")

        disciplina_existente = Disciplina.objects.filter(nome=nome).first()
        if disciplina_existente:
            return HttpResponse('Já existe uma disciplina com esse nome')
        
        nova_disciplina = Disciplina(nome=nome)        
        nova_disciplina.save()
        return redirect('auth:feed2')
    
    else:
        return render(request, 'nova_disciplina.html')

def filtrar_disciplina(request, nome_disciplina):
    disciplina = get_object_or_404(Disciplina, nome=nome_disciplina)
    disciplinas = Disciplina.objects.all()  # Obtém as disciplinas

    posts = Post.objects.filter(disciplinas=disciplina).order_by('-date')
    context = {
        'posts': posts,
        'nome_disciplina': nome_disciplina,
        'disciplinas': disciplinas,        

    }
    return render(request, 'filtrado.html', context)

def exibir_respostas(request, post_id):
    post = Post.objects.get(id=post_id)
    respostas = Respostas.objects.filter(post=post).order_by('-date')
    context = {'post': post, 'respostas': respostas}
    
    return render(request, 'respostas.html', context)    
    
@login_required(login_url="/auth/login/")
def enviar_resposta(request, post_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        author = request.user  
        
        post = get_object_or_404(Post, pk=post_id) 
        resposta = Respostas(author=author, content=content, post=post)
        resposta.save()
        return redirect('auth:exibir_respostas', post_id=post.id)
    else:
        return HttpResponse('Método não permitido', status=405)
    

@login_required(login_url="/auth/login/")
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.user == post.author or request.user.is_superuser:
        post.delete()
        return redirect('auth:feed2')
    else:
        return HttpResponseForbidden('Você não tem permissão para excluir este post')

@login_required(login_url="/auth/login/")
def delete_comment(request, comment_id):
    comentario = get_object_or_404(Respostas, pk=comment_id)

    if request.user == comentario.author or request.user.is_superuser:
        comentario.delete()
        return redirect('auth:exibir_respostas', comentario.post.id)  
    else:
        return HttpResponseForbidden('Você não tem permissão para excluir este comentário')


@login_required(login_url="/auth/login/")
def perfil(request, user_id):
    # Buscar o usuário com base no user_id
    usuario = get_object_or_404(User, pk=user_id)

    # Você quer as postagens do usuário, então você filtra por author
    posts_do_usuario = Post.objects.filter(author=usuario).order_by('-date')

    pesquisa = request.GET.get('pesquisa', '')  
    disciplinas = Disciplina.objects.all()

    # Se há uma pesquisa, filtra adicionalmente as postagens por conteúdo
    if pesquisa:
        posts_do_usuario = posts_do_usuario.filter(content__icontains=pesquisa)
    
    context = {
        'posts': posts_do_usuario,  # Use as postagens do usuário
        'disciplinas': disciplinas,
        'usuario': usuario  # Renomeei para evitar confusão com request.user
    }
    return render(request, 'meu_perfil.html', context)

@login_required(login_url="/auth/login/")
def editar_perfil(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)
    if request.user != usuario:
        return HttpResponseForbidden('Você não tem permissão para editar este perfil')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        foto_perfil = request.FILES.get('foto_perfil')
        
        usuario.username = username
        usuario.email = email
        usuario.save()
        
        if foto_perfil:
            usuario.pessoa.foto_perfil = foto_perfil
            usuario.pessoa.save()
        
        return redirect('auth:perfil', user_id=usuario.id)

    context = {
        'usuario': usuario
    }
    return render(request, 'editar_perfil.html', context)


