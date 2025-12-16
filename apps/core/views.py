from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

# def register_player(request):
#     if request.method == 'POST':
#         #inicia a sessão
#         request.session['player_name'] = request.POST.get('player_name')
#         request.session['stage'] = 1 # Estágio 1 = Hardware
#         return redirect('hardware:room') # Redireciona para o app Hardware
#     return redirect('core:index')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def victory(request):
    # Só acessa se completou o estágio 3 (Excel)
    # if request.session.get('stage', 0) < 4:
    #     return redirect('core:index')
    
    # return render(request, 'core/victory.html', {
    #     'name': request.session.get('player_name')
    # })
    return render(request, 'core/victory.html')