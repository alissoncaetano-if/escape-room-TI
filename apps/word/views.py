from django.shortcuts import render, redirect
from .models import WordTerm

def room(request):
    # Estágio 5: Word
    if request.session.get('stage', 1) != 5:
        return redirect('core:dashboard')

    # (Lógica da pergunta mantém igual)
    question_id = request.session.get('word_question_id')
    if not question_id:
        term = WordTerm.objects.order_by('?').first()
        if not term:
            return render(request, 'word/room.html', {'error': 'Sem dados.'})
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
        if answer == term.term.strip().lower():
            # FIM DO JOGO
            request.session['stage'] = 6 # Vitoria
            if 'word_question_id' in request.session:
                del request.session['word_question_id']
            request.session.modified = True
            return redirect('core:victory')
        else:
            error = "COMANDO INCORRETO."
    
    return render(request, 'word/room.html', {'term': term, 'error': error})