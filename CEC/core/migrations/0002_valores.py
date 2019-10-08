# Generated by Django 2.2.4 on 2019-10-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(verbose_name='Título do valor')),
            ],
            options={
                'verbose_name': 'Valor',
                'verbose_name_plural': 'Valores',
            },
        ),
    ]