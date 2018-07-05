from django.shortcuts import render, get_object_or_404
from .models import Pal
# Create your views here.

def indexView(request):
    return render(request, 'pals/index.html')

def pals_list(request):
    pals = Pal.objects.all()
    return render(request,'pals/pals_list.html',{'pals':pals})

def pal_profile(request,name):
    pal = get_object_or_404(Pal,name=name)
    return render(request, 'pals/pal_profile.html', {'pal':pal})