from django.shortcuts import render
from serv import views

# Create your views here.
def services(request):
    context = {'services' : 'active'}
    return render(request, 'serv/services.html', context)