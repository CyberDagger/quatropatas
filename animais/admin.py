from django.contrib import admin
from .models import Animal, Comentario, Adocao

class ComentarioInline(admin.StackedInline):
    model = Comentario
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome', 'slug', 'especie', 'raca', 'genero', 'idade', 'descricao', 'imagem']}),
    ]
    inlines = [ComentarioInline]

# Register your models here.
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Adocao)
