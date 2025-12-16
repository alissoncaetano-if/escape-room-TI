from django.db import models

# Create your models here.
class Component(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Fácil'),
        (2, 'Médio'),
        (3, 'Difícil'),
    ]

    name = models.CharField("Nome da Peça", max_length=100) # Ex: CPU, Memória RAM
    description = models.TextField("Função/Descrição") # Ex: Responsável pelo processamento...
    image = models.ImageField("Foto da Peça", upload_to="hardware_images/", blank=True, null=True)

    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Componente de Hardware"
        verbose_name_plural = "Componentes de Hardware"
        