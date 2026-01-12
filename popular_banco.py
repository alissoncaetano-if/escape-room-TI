import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'missao_tech.settings')
django.setup()

from apps.hardware.models import Component
from apps.word.models import WordTerm
from apps.excel.models import ExcelChallenge

def populate():
    print("Criando dados de Hardware...")
    Component.objects.get_or_create(name="CPU", description="O cérebro do computador, processa dados.")
    Component.objects.get_or_create(name="RAM", description="Memória temporária de acesso rápido.")

    print("Criando dados de Word...")
    WordTerm.objects.get_or_create(term="Negrito", clue="Deixa o texto mais escuro e grosso.")
    WordTerm.objects.get_or_create(term="Salvar", clue="Persiste as alterações do documento no disco (Ctrl+B).")

    print("Criando dados de Excel...")
    ExcelChallenge.objects.get_or_create(
        scenario="Calcule a média das notas nas células A1, A2 e A3.",
        correct_formula="=MEDIA(A1:A3)",
        accepted_variations="=media(a1:a3), =MÉDIA(A1:A3)"
    )

    print("Concluído! Agora você pode jogar.")

if __name__ == '__main__':
    populate()