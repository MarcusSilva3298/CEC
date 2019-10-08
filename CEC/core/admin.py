from django.contrib import admin
from .models import Ensino, Evento, PropostaPedagogica, Aplicativo, Galeria, Contatos

# Register your models here.
admin.site.register(Ensino)
admin.site.register(Evento)
admin.site.register(PropostaPedagogica)
admin.site.register(Aplicativo)
admin.site.register(Galeria)
admin.site.register(Contatos)