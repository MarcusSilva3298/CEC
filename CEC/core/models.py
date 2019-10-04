from django.db import models

# Create your models here.
class Ensino(models.Model):
    titulo = models.CharField('Título', default ='Ensino', max_length = 100)
    sub_tit = models.CharField('Subtítulo', default = 'Conheça o método de ensino que usamos :', max_length = 100)
    desc = models.TextField('Descrição da seção', default = 'Descrição da seção')

    class Meta:
        verbose_name = 'Ensino'
        verbose_name_plural = 'Ensino'

    def __str__(self):
        return self.titulo
