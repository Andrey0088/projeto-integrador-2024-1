# Generated by Django 5.0.2 on 2024-02-25 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_pessoa_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='usuarios\\static\\ppic.png', null=True, upload_to='perfil/'),
        ),
    ]
