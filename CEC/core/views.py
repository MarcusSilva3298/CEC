from django.shortcuts import render, HttpResponse
from .models import Ensino, Evento, PropostaPedagogica, Valores, Aplicativo, Galeria, Contatos
from .forms import Matricula, Contato

# Create your views here.
def home(request):
    data = {}

    #Impotação dos models
    data['Ensino'] = Ensino.objects.all()
    data['Evento'] = Evento.objects.all()
    data['Proposta_Pedagogica'] = PropostaPedagogica.objects.all()
    data['Valores'] = Valores.objects.all()
    data['Aplicativo'] = Aplicativo.objects.all()
    data['Galeria'] = Galeria.objects.all()
    data['Contatos'] = Contatos.objects.all()

    #Utilização dos forms
    if request.method is 'POST':
        #Importação dos forms
        form = Matricula(request.POST)
        form1 = Contato(request.POST)

        if form.is_valid():
            data['is_valid'] = True
            print(form.cleaned_data)
            form.send_mail()

            #RESETANDO OS FORMS
            form = Matricula()
            form1 =  Contato()

        if form1.is_valid():
            data['is_valid'] = True
            print(form1.cleaned_data)
            form1.send_mail()

            #RESETANDO OS FORMS
            form = Matricula()
            form1 =  Contato()
    else:
        form = Matricula()
        form1 =  Contato()


    return HttpResponse(data)
    #return render(request, 'index.html', data)