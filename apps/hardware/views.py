from django.shortcuts import render, redirect
from .models import Component

def store(request):
    # Estágio 2: Loja
    if request.session.get('stage', 1) != 2:
        return redirect('core:dashboard')

    if request.method == 'POST':
        choice = request.POST.get('component_choice')
        if choice == 'cpu':
            request.session['stage'] = 3 # Vai pro Lab
            request.session.modified = True
            return redirect('core:dashboard')
        else:
            return render(request, 'hardware/store.html', {'error': 'Componente errado. O sistema precisa de CÉREBRO (Processamento).'})

    return render(request, 'hardware/store.html')

def room(request):
    # Estágio 3: Montagem
    if request.session.get('stage', 1) != 3:
        return redirect('core:dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'install':
            request.session['stage'] = 4 # Vai pro Excel
            request.session.modified = True
            return redirect('core:dashboard') 

    try:
        cpu = Component.objects.get(name__icontains="CPU")
    except:
        cpu = None

    return render(request, 'hardware/room.html', {'component': cpu})