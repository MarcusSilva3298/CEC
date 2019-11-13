from django import forms
from django.core.mail import send_mail, EmailMessage
from ..settings import DEFAULT_FROM_EMAIL, CONTACT_EMAIL

class Matricula(forms.Form):
    #serie choices
    series = [
        ('', 'Série'),
        ('Tempo Integral', 'Tempo Integral'),
        ('Fase 1', 'Fase 1 (A partir de 1 ano e 8 Meses)'),
        ('Fase 2', 'Fase 2 (A partir de 2 anos)'),
        ('Fase 3', 'Fase 3 (A partir de 3 anos)'),
        ('Fase 4', 'Fase 4 (A partir de 4 anos)'),
        ('Fase 5', 'Fase 5 (A partir de 5 anos)'),
        ('1º Ano', '1º Ano'),
        ('2º Ano', '2º Ano'),
        ('3º Ano', '3º Ano'),
        ('4º Ano', '4º Ano'),
        ('5º Ano', '5º Ano'),
        ('6º Ano', '6º Ano'),
        ('7º Ano', '7º Ano'),
        ('8º Ano', '8º Ano'),
        ('9º Ano', '9º Ano'),
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
