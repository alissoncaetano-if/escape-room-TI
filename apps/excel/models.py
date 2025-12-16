from django.db import models

# Create your models here.
class ExcelChallenge(models.Model):
    FUNCTION_TYPE = [
        ('MATH', 'Matemática'),
        ('LOGIC', 'Lógica (SE)'),
        ('TEXT', 'Texto'),
    ]

    scenario = models.TextField("Cenário do Problema")
    # Ex: "Você precisa somar as células A1 até A10"

    data_preview = models.ImageField("Print da Planilha", upload_to='excel_screens/', blank=True)
    # Mostra a imagem da tabela para ele entender o contexto

    correct_formula = models.CharField("Fórmula Correta", max_length=200)
    # Ex: =SOMA(A1:A10)

    accepted_variations = models.TextField("Variações aceitas", help_text="Separe por vírgula")
    # Ex: =soma(a1:a10), =SOMA( A1:A10 ) -> Para facilitar a validação

    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.scenario[:50]