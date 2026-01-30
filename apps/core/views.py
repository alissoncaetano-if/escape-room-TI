from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    return render(request, 'core/index.html')

@login_required
def dashboard(request):
    # Se não tiver estágio, define como 1
    current_stage = request.session.get('stage', 1)
    
    context = {
        'stage': current_stage,
        'player_name': request.user.username
    }
    return render(request, 'core/dashboard.html', context)

@login_required
def control_room(request):
    # Estágio 1: Diagnóstico
    if request.session.get('stage', 1) != 1:
        return redirect('core:dashboard')

    if request.method == 'POST':
        # Se o usuário identificou o erro (CPU)
        if request.POST.get('action') == 'diagnose_cpu':
            request.session['stage'] = 2 # Avança para a Loja
            request.session.modified = True
            return redirect('core:dashboard')

    return render(request, 'core/control_room.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            request.session['stage'] = 1
            return redirect('core:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def victory(request):
    return render(request, 'core/victory.html')