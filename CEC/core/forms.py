from django import forms
from django.core.mail import send_mail, EmailMessage
from ..settings import DEFAULT_FROM_EMAIL, CONTACT_EMAIL

class Matricula(forms.Form):
    #serie choices
    series = [
        ('', 'Série'),
        ('0', 'Pré infantil'),
        ('1', 'fundamental 1'),
        ('2', 'fundamental 2')
    ]

    nome_resp = forms.CharField(
        error_messages = {'required': 'Por favor, insira seu nome'},
        widget = forms.TextInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite o nome do responsável'
        })
    )
    telefone = forms.CharField(
        error_messages = {'required': 'Por favor, insira seu telefone'},
        widget = forms.TextInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite o telefone do responsável'
        })
    )
    email = forms.EmailField(
        error_messages = {'required': 'Por favor, insira seu email'},
        widget = forms.EmailInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite o email do responsável'
        })
    )
    nome_cri = forms.CharField(
        error_messages = {'required': 'Por favor, insira o nome da ciança'},
        widget = forms.TextInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite o nome da criança'
        })
    )
    serie = forms.ChoiceField(
        choices = series,
        error_messages = {'required': 'Por favor, insira a série da criança'},
        widget = forms.Select( attrs= {
            'class': 'form-control form'
        })
    )

    def send_mail(self):
        print('---------Email Matricula---------')
        mensagem = 'Nome: %(nome_resp)s;\nTelefone: %(telefone)s;\nE-mail: %(email)s;\nNome da Criança: %(nome_cri)s;\nSerie: %(serie)s'
        subject = self.cleaned_data['email']
        context = {
            'nome_resp': self.cleaned_data['nome_resp'],
            'email': self.cleaned_data['email'],
            'telefone': self.cleaned_data['telefone'],
            'nome_cri': self.cleaned_data['nome_cri'],
            'serie': self.cleaned_data['serie']
        }
        mensagem = mensagem % context
        print(f'{subject}\n{mensagem}')
        mail = EmailMessage( subject = subject, body = mensagem, from_email = DEFAULT_FROM_EMAIL, to = [CONTACT_EMAIL])
        mail.send(fail_silently=False)


class Contato(forms.Form):
    nome = forms.CharField(
        error_messages = {'required': 'Por favor, insira seu nome'},
        widget = forms.TextInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite seu nome'
        })
    )
    telefone = forms.CharField(
        error_messages = {'required': 'Por favor, insira seu telefone'},
        widget = forms.TextInput( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite seu telefone'
        })
    )
    mensagem = forms.CharField(
        error_messages = {'required': 'Por favor, insira uma mensagem'},
        widget = forms.Textarea( attrs= {
            'class': 'form-control',
            'placeholder': 'Digite sua mensagem'
        })
    )

    def send_mail(self):
        print('---------Email Contato---------')

        mensagem = 'Nome: %(nome)s;\nTelefone: %(telefone)s;\nMensagem: %(mensagem)s'
        subject = self.cleaned_data['nome']
        context = {
            'telefone': self.cleaned_data['telefone'],
            'nome': self.cleaned_data['nome'],
            'mensagem': self.cleaned_data['mensagem']
        }
        mensagem = mensagem % context
        print(f'{mensagem}')
        mail = EmailMessage(subject = subject, body = mensagem, from_email = DEFAULT_FROM_EMAIL, to = [CONTACT_EMAIL])
        mail.send(fail_silently=False)