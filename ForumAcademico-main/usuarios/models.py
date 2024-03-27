from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='perfil/', default='usuarios/static/ppic.png')
    qualificacao = models.CharField(max_length=50)
    semestre = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)  # Adicione esta linha para o e-mail

    
    def __str__(self):
        return self.user.username

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    disciplinas = models.ManyToManyField(Disciplina, related_name='posts')

    def __str__(self):
        return self.content[:50]  


class Respostas(models.Model):
    author = models.ForeignKey(User, related_name='respostas', on_delete=models.CASCADE)
    content = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='respostas', on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username
