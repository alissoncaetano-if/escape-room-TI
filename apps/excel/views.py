from django.shortcuts import render, redirect

# Create your views here.
# ... imports
def room(request):
    if request.session.get('stage', 0) != 3: # Verifica estágio 3
        return redirect('core:index')

    if request.method == 'POST':
        if request.POST.get('answer') == 'soma': # Resposta do Excel
            request.session['stage'] = 4 # Finalizou
            return redirect('core:victory') # Vai para tela final no Core
    
    return render(request, 'excel/room.html')