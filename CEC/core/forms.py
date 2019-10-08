from django import forms
from django.core.mail import send_mail, EmailMessage

class Matricula(forms.Form):
    nome_resp = forms.CharField()
    telefone = forms.CharField()
    email = forms.EmailField()
    nome_cri = forms.CharField()

class Contato(forms.Form):
    nome = forms.CharField()
    telefone = forms.CharField()
    mensagem = forms.CharField()