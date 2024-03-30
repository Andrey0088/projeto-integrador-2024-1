# Generated by Django 5.0.2 on 2024-03-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_remove_pessoa_email_remove_pessoa_senha_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='foto_perfil',
        ),
        migrations.AddField(
            model_name='post',
            name='disciplinas',
            field=models.ManyToManyField(related_name='posts', to='usuarios.disciplina'),
        ),
    ]