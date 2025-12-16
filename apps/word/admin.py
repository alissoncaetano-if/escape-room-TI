from django.contrib import admin
from .models import WordTerm, GlitchChallenge

# Register your models here.
@admin.register(WordTerm)
class WordTermAdmin(admin.ModelAdmin):
    list_display = ('term', 'category', 'clue_preview')
    list_filter = ('category',)
    search_fields = ('term',)

    def clue_preview(self, obj):
        return obj.clue[:50] + "..." if len(obj.clue) > 50 else obj.clue
    clue_preview.short_description = "Dica"

@admin.register(GlitchChallenge)
class GlitchChallengeAdmin(admin.ModelAdmin):
    list_display = ('title', 'correct_answer')