# Generated by Django 5.1.3 on 2024-11-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_alter_estudiante_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.URLField(default='https://st3.depositphotos.com/16203680/19307/v/950/depositphotos_193076602-stock-illustration-question-mark-hand-drawn-symbol.jpg'),
        ),
    ]
