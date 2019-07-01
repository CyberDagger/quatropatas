from django import forms
from . import models
from phonenumber_field.formfields import PhoneNumberField

class CreateComentario(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields = ['texto']

class CreateAdocao(forms.ModelForm):
    class Meta:
        model = models.Adocao
        fields = ['telefone', 'data', 'hora']
