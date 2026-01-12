from django.shortcuts import render, redirect
from .models import ExcelChallenge

def room(request):
    # Verifica estágio 3
    if request.session.get('stage', 1) != 3:
        return redirect('core:dashboard')

    question_id = request.session.get('excel_question_id')
    
    if not question_id:
        challenge = ExcelChallenge.objects.order_by('?').first()
        if not challenge:
            return render(request, 'excel/room.html', {'error': 'Sem dados no DB.'})
        request.session['excel_question_id'] = challenge.id
    else:
        try:
            challenge = ExcelChallenge.objects.get(id=question_id)
        except ExcelChallenge.DoesNotExist:
            del request.session['excel_question_id']
            return redirect('excel:room')

    error = None
    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip().lower()
        # Remove espaços extras da resposta do aluno para facilitar comparação
        answer = answer.replace(" ", "")
        
        # Prepara variações aceitas
        correct_list = [x.strip().lower().replace(" ", "") for x in challenge.accepted_variations.split(',')]
        # Adiciona a fórmula principal também
        correct_list.append(challenge.correct_formula.strip().lower().replace(" ", ""))

        if answer in correct_list:
            request.session['stage'] = 4 # Vitória!
            if 'excel_question_id' in request.session:
                del request.session['excel_question_id']
            request.session.modified = True
            return redirect('core:victory')
        else:
            error = "ERRO DE CÁLCULO: Fórmula incorreta."
    
    return render(request, 'excel/room.html', {'challenge': challenge, 'error': error})