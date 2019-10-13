from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from .models import Ensino, Evento, PropostaPedagogica, Valores, Aplicativo, Galeria, Contatos, Projetos
from .forms import Matricula, Contato

# Create your views here.
def home(request):
    #Def dos Dic's
    models_context = {}
    forms_context = {}

    #Impotação dos models
    models_context['Ensino'] = Ensino.objects.all()
    models_context['Evento'] = Evento.objects.all()
    models_context['Proposta_Pedagogica'] = PropostaPedagogica.objects.all()
    models_context['Valores'] = Valores.objects.all()
    models_context['Aplicativo'] = Aplicativo.objects.all()
    models_context['Galeria'] = Galeria.objects.all()
    models_context['Contatos'] = Contatos.objects.all()
    models_context['Projetos'] = Projetos.objects.order_by('-start_date')

    #Utilização dos forms
    if request.method is 'POST':
        #Importação dos forms
        form = Matricula(request.POST)
        form1 = Contato(request.POST)

        if form.is_valid():
            forms_context['is_valid'] = True
            print(form.cleaned_data)
            form.send_mail()

            #RESETANDO OS FORMS
            form = Matricula()
            form1 =  Contato()

        if form1.is_valid():
            forms_context['is_valid'] = True
            print(form1.cleaned_data)
            form1.send_mail()

            #RESETANDO OS FORMS
            form = Matricula()
            form1 =  Contato()
    else:
        form = Matricula()
        form1 =  Contato()

    data = { **models_context, **forms_context}
    return render(request, 'index.html', data)


def blogProjetos(request):
    #Def dos Dic's
    models_context = {}
    forms_context = {}

    #Def paginador
    proj_list = Projetos.objects.order_by('-start_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(proj_list, 6)
    try:
        proj = paginator.page(page)
    except PageNotAnInteger:
        proj = paginator.page(1)
    except EmptyPage:
        proj = paginator.page(paginator.num_pages)

    #Importação dos models
    models_context['Contatos'] = Contatos.objects.all()
    models_context['Projetos'] = proj

    #Utilização do form
    if request.method is 'POST':
        form1 = Contato(request.POST)

        if form1.is_valid:
            forms_context['is_valid'] = True
            print(form1.cleaned_data)
            form1.send_mail()

            #RESETANDO OS FORMS
            form1 = Contato()
    else:
        form1 = Contato()

    data = {**models_context, **forms_context}
    return render(request, 'blog.html', data)


def postProjeto(request, slug):
    models_context = {}
    forms_context = {}

    models_context['Contatos'] = Contatos.objects.all()
    
    #Utilização do form
    if request.method is 'POST':
        form1 = Contato(request.POST)

        if form1.is_valid:
            forms_context['is_valid'] = True
            print(form1.cleaned_data)
            form1.send_mail()

            #RESETANDO OS FORMS
            form1 = Contato()
    else:
        form1 = Contato()

    data = {**models_context, **forms_context}

    return render(request, 'post.html', data)
