from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from MyMomentumApp.models import Instrument, Price

def index(request):
    i = Instrument.objects.all()
    return render(request, 'test1.html', {'instruments': i})