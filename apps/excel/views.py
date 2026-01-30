from django.shortcuts import render, redirect
from .models import ExcelChallenge

def room(request):
    # Estágio 4: Excel
    if request.session.get('stage', 1) != 4:
        return redirect('core:dashboard')

    # (Lógica da pergunta mantém igual, só mudei o estágio final no sucesso)
    question_id = request.session.get('excel_question_id')
    if not question_id:
        challenge = ExcelChallenge.objects.order_by('?').first()
        if not challenge:
            return render(request, 'excel/room.html', {'error': 'Sem dados.'})
        request.session['excel_question_id'] = challenge.id
    else:
        try:
            challenge = ExcelChallenge.objects.get(id=question_id)
        except ExcelChallenge.DoesNotExist:
            del request.session['excel_question_id']
            return redirect('excel:room')

    error = None
    if request.method == 'POST':
        answer = request.POST.get('answer', '').strip().lower().replace(" ", "")
        correct_list = [x.strip().lower().replace(" ", "") for x in challenge.accepted_variations.split(',')]
        correct_list.append(challenge.correct_formula.strip().lower().replace(" ", ""))

        if answer in correct_list:
            request.session['stage'] = 5 # Vai pro Word
            if 'excel_question_id' in request.session:
                del request.session['excel_question_id']
            request.session.modified = True
            return redirect('core:dashboard')
        else:
            error = "FÓRMULA INVÁLIDA."
    
    return render(request, 'excel/room.html', {'challenge': challenge, 'error': error})