from django.shortcuts import render, redirect

# Create your views here.
# ... imports
def room(request):
    if request.session.get('stage', 0) != 2: # Verifica estágio 2
        return redirect('core:index') # Ou lógica para redirecionar para a sala certa

    if request.method == 'POST':
        if request.POST.get('answer') == 'negrito': # Resposta do Word
            request.session['stage'] = 3
            return redirect('excel:room') # Vai para Excel
    
    return render(request, 'word/room.html')