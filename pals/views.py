from django.shortcuts import render, get_object_or_404
from .models import Pal, Quiz
from django.template import RequestContext
# Create your views here.

def indexView(request):
    context = RequestContext(request)
    default_quiz = get_object_or_404(Quiz, name='default')
    return render(request, 'pals/index.html', {'default_quiz':default_quiz})

def pals_list(request):
    pals = Pal.objects.all()
    return render(request,'pals/pals_list.html',{'pals':pals})

def pal_profile(request,name):
    pal = get_object_or_404(Pal,name=name)
    return render(request, 'pals/pal_profile.html', {'pal':pal})

def quizView(request, default_quiz):
    quiz = get_object_or_404(Quiz, name=default_quiz)
    return render(request, 'pals/quiz.html',
        {'question':quiz.get_current_question()})