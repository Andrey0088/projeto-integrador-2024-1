# Generated by Django 5.0.2 on 2024-03-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_remove_disciplina_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='semestre',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
