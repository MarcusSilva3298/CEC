from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Projetos(models.Model):
    titulo = models.CharField('Titulo do Projeto', max_length = 100, default = 'Projeto', unique = True)
    atalho = models.SlugField('Atalho', max_length = 100, unique = True)
    desc = models.TextField('Descrição rápida do projeto', default = 'Descrição do projeto', max_length = 260)
    content = RichTextField('Conteúdo do Post do Projeto')
    start_date = models.DateField('Data de criação do Post', auto_now_add = True)
    img_ic = models.ImageField(verbose_name = 'Imagem ícone do projeto', upload_to = 'img/projeto/icone')
    img_bn = models.ImageField(verbose_name = 'Imagem banner do projeto', upload_to = 'img/projeto/banner')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return f'Projetos/{self.atalho}'

class Ensino(models.Model):
    subtitulo = models.CharField('Subtítulo', max_length = 100, default = 'Subtítulo')
    desc = models.TextField('Descrição da seção')

    class Meta:
        verbose_name = 'Ensino'
        verbose_name_plural = 'Ensino'

    def __str__(self):
        return 'Ensino'

class Evento(models.Model):
    titulo = models.CharField('Título do evento', default = 'Próximo Evento', max_length = 50)
    img = models.ImageField(verbose_name = 'Imagem do evento', upload_to = 'img/evento')
    desc = models.TextField('Descrição do evento', max_length = 483)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Evento'

    def __str__(self):
        return self.titulo

class PropostaPedagogica(models.Model):
    desc = models.TextField('Texto da Proposta Pedagócia')
    img = models.ImageField(verbose_name = 'Imagem da Proposta Pedagógica', upload_to = 'img/proposta_pedagógica')

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
    img = models.ImageField(verbose_name = 'Imagem do Aplicativo', upload_to = 'img/aplicativo')
    playstore = models.URLField('Link para Download do App na PlayStore', max_length = 10000, default = 'http://')
    ios = models.URLField('Link para Download do App na AppStore', max_length = 10000, default = 'http://')

    class Meta:
        verbose_name = 'Aplicativo'
        verbose_name_plural = 'Aplicativo'

    def __str__(self):
        return 'Aplicativo'

class Galeria(models.Model):
    titulo = models.CharField('Título da imagem', default = 'Imagem', max_length = 30)
    img = models.ImageField(verbose_name = 'Imagem para galeria', upload_to = 'img/galeria')
    class Meta:
        verbose_name = 'Imagem da galeria'
        verbose_name_plural = 'Imagens da galeria'

    def __str__(self):
        return self.titulo

class Contatos(models.Model):
    telefone = models.CharField('Telefone para Contato', max_length = 30)
    email = models.EmailField('Email para Contato', max_length = 50)
    wpp = models.URLField('Link para WhatsApp', max_length = 100, default = 'http://')
    insta = models.URLField('Link para Instagram', max_length = 100, default = 'http://')
    face = models.URLField('Link para Facebook', max_length = 100, default = 'http://')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contato'

    def __str__(self):
        return 'Informações para contato'