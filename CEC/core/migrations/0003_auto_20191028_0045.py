# Generated by Django 2.2.4 on 2019-10-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191024_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='desc',
            field=models.TextField(default='Descrição do projeto', max_length=260, verbose_name='Descrição rápida do projeto'),
        ),
    ]