from django.contrib import admin
from .models import Component

# Register your models here.
@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'has_image') # O que aparece na lista
    list_filter = ('difficulty',) # Filtro Lateral
    search_fields = ('name', 'description')

    # Função auxiliar para mostrar se tem imagem cadastrada
    def has_image(self, obj):
        return "Sim" if obj.image else "Não"
    has_image.short_description = "Possui Imagem?"