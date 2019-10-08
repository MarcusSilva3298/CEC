from django.db import models

# Create your models here.
class Ensino(models.Model):
    subtitulo = models.CharField('Subtítulo', max_length = 100)
    desc = models.TextField('Descrição da seção')

    class Meta:
        verbose_name = 'Ensino'
        verbose_name_plural = 'Ensino'

    def __str__(self):
        return 'Ensino'

class Evento(models.Model):
    titulo = models.CharField('Título do evento', default = 'Próximo Evento', max_length = 50)
    desc = models.TextField('Descrição do evento', default = 'Descrição do Evento')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Evento'

    def __str__(self):
        return self.titulo

class PropostaPedagogica(models.Model):
    desc = models.TextField('Texto da Proposta Pedagócia')

    class Meta:
        verbose_name = 'Proposta Pedagógia'
        verbose_name_plural = 'Proposta Pedagógica'

    def __str__(self):
        return 'Proposta Pedagógica'

class Valores(models.Model):
    titulo = models.CharField('Título do valor', max_length = 30)
    
    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'

    def __str__(self):
        return self.titulo

class Aplicativo(models.Model):
    desc = models.TextField('Texto do Conheça Nosso Aplicativo')

    class Meta:
        verbose_name = 'Aplicativo'
        verbose_name_plural = 'Aplicativo'

    def __str__(self):
        return 'Aplicativo'

class Galeria(models.Model):
    titulo = models.CharField('Título da imagem', default = 'Imagem', max_length = 30)
    img = models.ImageField('Imagem da galeria')
    class Meta:
        verbose_name = 'Imagem da galeria'
        verbose_name_plural = 'Imagens da galeria'

    def __str__(self):
        return self.titulo

class Contatos(models.Model):
    telefone = models.CharField('Telefone para Contato', max_length = 30)
    email = models.EmailField('Email para Contato', max_length = 50)
    wpp = models.URLField('Link para WhatsApp', max_length = 100)
    insta = models.URLField('Link para Instagram', max_length = 100)
    face = models.URLField('Link para Facebook', max_length = 100)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contato'

    def __str__(self):
        return 'Informações para contato'