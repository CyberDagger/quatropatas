from django.shortcuts import render, redirect
from .models import Animal, Adocao
from django.http import HttpResponse
from . import forms
from .forms import CreateAdocao
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from doacao.models import Doacao

# Create your views here.
def index(request):
    animais = Animal.objects.all()
    try:
        doacao = Doacao.objects.latest()
    except Doacao.DoesNotExist:
        doacao = None
    return render(request, 'animais/index.html', {'animais': animais, 'doacao': doacao})

def animal_details(request, slug):
    animal = Animal.objects.get(slug=slug)
    try:
        adocao = Adocao.objects.get(animal=animal)
    except Adocao.DoesNotExist:
        adocao = None
    if request.method == 'POST':
        form = forms.CreateComentario(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.animal = animal
            instance.autor = request.user
            instance.save()
            return redirect('animais:animal', animal.slug)
    else:
        form = forms.CreateComentario()
    return render(request, 'animais/animal.html', {'animal': animal, 'adocao': adocao, 'form': form})

@login_required(login_url='/conta/login/')
def adocao(request, slug):
    animal = Animal.objects.get(slug=slug)
    # adocao = Adocao()
    # adocao.animal = Animal.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateAdocao(request.POST)
        if form.is_valid():
            adocaoToSave = Adocao()
            adocaoToSave.telefone = request.POST.get('telefone')
            adocaoToSave.data = request.POST.get('data')
            adocaoToSave.hora = request.POST.get('hora')
            adocaoToSave.pessoa = request.user
            adocaoToSave.animal = Animal.objects.get(slug=slug)
            adocaoToSave.save()
            # redireciona para ecra de com mensagem de sucesso adocao agendada ou criada.
            messages.success(request, 'Form submission successful')
            return render(request, 'animais/adocao.html')
        else:
            # apresenta ecra de erro
            error_message = form.errors
            return render(request,'animais/adocao.html', {'form': form, 'error_message': error_message} )
    else: # 1º Acesso à página
        success_message=''
        if 'sucesso' in request.GET:
            # passa para view campo
            success_message = 'Adoção criada!'

        form = CreateAdocao()

        return render(request, 'animais/adocao.html', {
            'form': form,
            'animal': animal,
            'success_message': success_message
        })
