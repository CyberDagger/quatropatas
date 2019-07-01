from django.shortcuts import render, redirect
from .models import Doacao
from .forms import DoacaoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
@login_required(login_url='/conta/login/')
def doacao_view(request):
    # doacao = Doacao)
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            adocaoToSave = form.save(commit=False)
            adocaoToSave.utilizador = request.user
            adocaoToSave.save()
            messages.success(request, 'Form submission successful')

            # redireciona para ecra de com mensagem de sucesso doacao registada.
            return render(request, 'doacao/doacao.html')
        else:
            # apresenta ecra de erro
            error_message = form.errors
            return render(request,'doacao/doacao.html', {'form': form, 'error_message': error_message} )
    else: # 1º Acesso à página
        success_message=''

        form = DoacaoForm()

        return render(request, 'doacao/doacao.html', {
            'form': form,
            'success_message': success_message
        })
