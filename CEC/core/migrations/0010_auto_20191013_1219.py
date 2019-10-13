# Generated by Django 2.2.4 on 2019-10-13 15:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20191013_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='start_date',
            field=models.DateField(auto_now=True, verbose_name='Data de criação do Post'),
        ),
        migrations.AlterField(
            model_name='projetos',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Conteúdo do Post do Projeto'),
        ),
    ]