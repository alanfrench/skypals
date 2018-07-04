from django.shortcuts import render
from .models import Pal
# Create your views here.

def pals_list(request):
    pals = Pal.objects.all()
    return render(request,'pals/pals_list.html',{'pals':pals})