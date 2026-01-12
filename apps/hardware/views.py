from django.shortcuts import render, redirect
from .models import Component
import random

def room(request):
    # 1. Segurança: Verifica se o jogador está na fase 1
    # Se a sessão não tiver 'stage', define como 1 (início)
    if request.session.get('stage', 1) != 1:
        return redirect('core:dashboard') # Manda pro painel se não for a fase certa

    # 2. Lógica da Pergunta (Persistência)
    # Verifica se já existe uma pergunta ativa na sessão para esta sala
    question_id = request.session.get('hardware_question_id')
    
    if not question_id:
        # Se não tem pergunta, sorteia uma do banco
        component = Component.objects.order_by('?').first()
        if not component:
            return render(request, 'hardware/room.html', {'error': 'Banco de dados vazio! Contate o professor.'})
        
        # Salva o ID na sessão
        request.session['hardware_question_id'] = component.id
    else:
        # Se já tem, busca ela no banco
        try:
            component = Component.objects.get(id=question_id)
        except Component.DoesNotExist:
            # Caso o ID seja inválido (ex: deletado do banco), limpa e recarrega
            del request.session['hardware_question_id']
            return redirect('hardware:room')

    error = None

    # 3. Processamento da Resposta
    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip().lower()
        correct_name = component.name.strip().lower()

        if answer == correct_name:
            # ACERTOU:
            # 1. Atualiza o estágio para 2 (Word)
            request.session['stage'] = 2
            # 2. Limpa a pergunta atual da sessão para não travar nela se jogar de novo
            if 'hardware_question_id' in request.session:
                del request.session['hardware_question_id']
            request.session.modified = True
            
            # 3. Redireciona para a próxima sala
            return redirect('word:room')
        else:
            error = "ACESSO NEGADO: Componente incorreto."

    return render(request, 'hardware/room.html', {
        'component': component, 
        'error': error
    })