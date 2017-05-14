from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from MyMomentumApp.models import Instrument, Price, Universe
from yahoo_finance import Share

def index(request):
    
#    i = Instrument.objects.all()
    universe = request.GET.get('universe', '')
  
    if(universe == "HDAX"):
        url_name = "data/HDAX_universe.json"
    else:        
        url_name = "data/SP500_universe.json"
    
    return render(request, 'home.html', {'filename': url_name})