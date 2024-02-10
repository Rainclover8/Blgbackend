from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def yazilar(request):
    
    deneme = YazilarModels.objects.all()
    
    context = {
        'deneme':deneme
    }
    
    return render(request, 'yazilar.html', context)