from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    data = {'Hello World! :)'}

    return HttpResponse(data)
    #return render(request, 'index.html', data)