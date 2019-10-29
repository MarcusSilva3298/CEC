from django.contrib import admin
from .models import Ensino, Evento, PropostaPedagogica, Aplicativo, Galeria, Contatos, Valores, Projetos


class ProjetosAdmin(admin.ModelAdmin):
    prepopulated_fields = {"atalho": ["titulo"]}

admin.site.register(Projetos, ProjetosAdmin)
admin.site.register(Ensino)
admin.site.register(Evento)
admin.site.register(PropostaPedagogica)
admin.site.register(Aplicativo)
admin.site.register(Galeria)
admin.site.register(Contatos)
admin.site.register(Valores)