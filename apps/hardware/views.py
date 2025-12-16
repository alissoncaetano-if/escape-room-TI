from django.shortcuts import render, redirect

# Create your views here.
def room(request):
    # Segurança: Verifica se o jogador está na fase certa
    if request.session.get('stage', 0) != 1:
        # Se ele já passou, manda pra onde ele parou, ou volta para o início
        return redirect('core:index')
    
    error = None
    if request.method == 'POST':
        answer = request.POST.get('answer', '').lower.strip()

        # Lógica do Enigma
        if answer == 'cpu' or answer == 'processador':
            request.session['stage'] = 2 # Libera fase 2
            request.session.modified = True
            return redirect('word:room') # Manda para o app Word
        else:
            error = "Componente incorreto. O sistema não iniciou"
    
    return render(request, 'hardware/room.html', {'error': error})