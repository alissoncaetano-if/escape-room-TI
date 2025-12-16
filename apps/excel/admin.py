from django.contrib import admin
from .models import ExcelChallenge

# Register your models here.
@admin.register(ExcelChallenge)
class ExcelChallengeAdmin(admin.ModelAdmin):
    list_display = ('scenario_preview', 'correct_formula', 'difficulty')
    list_filter = ('difficulty',)
    search_fields = ('scenario', 'correct_formula')

    # Campo de ajuda para lembrar como cadastrar variações
    fieldsets = (
        (None, {
            'fields': ('scenario', 'data_preview', 'difficulty')
        }),
        ('Resposta', {
            'fields': ('correct_formula', 'accepted_variations'),
            'description': 'Em "Variações Aceitas", separe as respostas possíveis por vírgula.'
        }),
    )

    def scenario_preview(self, obj):
        return obj.scenario[:60] + "..."
    scenario_preview.short_description = "Cenário"