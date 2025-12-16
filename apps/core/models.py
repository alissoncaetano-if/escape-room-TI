from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField("Nome do Aluno", max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # Controle de progresso(qual sala ele está?)
    current_stage = models.IntegerField(default=1)

    # Pontuação
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - Sala {self.current_stage}"