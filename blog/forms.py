from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'telefone', 'cidade', 'mensagem']