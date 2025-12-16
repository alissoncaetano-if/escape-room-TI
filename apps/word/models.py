from django.db import models

# Create your models here.
class WordTerm(models.Model):
    term = models.CharField("Palavra/Comando", max_length=50) # Ex: Negrito, Justificar
    clue = models.CharField("Dica", max_length=255) # Ex: Deixa o texto mais escuro/grosso

    # Se quiser misturar mais temas depois
    category = models.CharField(max_length=50, default='Formatação')

    def __str__(self):
        return self.term
    
class GlitchChallenge(models.Model):
    """
    Desafio visual onde o aluno tem que achar o erro na imagem
    """
    title = models.CharField("Título do Erro", max_length=100)
    image_file = models.ImageField(upload_to='word_glitches/')
    correct_answer = models.CharField("Comando para corrigir", max_length=100) # Ex: Ctrl+Z

    def __str__(self):
        return self.title

