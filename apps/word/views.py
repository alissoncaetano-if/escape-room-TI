from django.shortcuts import render, redirect
from .models import WordTerm

def room(request):
    # Verifica estágio 2
    if request.session.get('stage', 1) != 2:
        return redirect('core:dashboard')

    # Busca ou Mantém a pergunta
    question_id = request.session.get('word_question_id')
    
    if not question_id:
        term = WordTerm.objects.order_by('?').first()
        if not term:
            return render(request, 'word/room.html', {'error': 'Sem dados no DB.'})
        request.session['word_question_id'] = term.id
    else:
        try:
            term = WordTerm.objects.get(id=question_id)
        except WordTerm.DoesNotExist:
            del request.session['word_question_id']
            return redirect('word:room')

    error = None
    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip().lower()
        correct = term.term.strip().lower()

        if answer == correct:
            request.session['stage'] = 3 # Vai para Excel
            if 'word_question_id' in request.session:
                del request.session['word_question_id']
            request.session.modified = True
            return redirect('excel:room')
        else:
            error = "SINTAXE INVÁLIDA: Comando não reconhecido."
    
    return render(request, 'word/room.html', {'term': term, 'error': error})