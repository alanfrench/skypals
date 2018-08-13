from django.shortcuts import render, get_object_or_404
from .models import Pal, Quiz, Question
from django.template import RequestContext
# stuff for forms
from .forms import QuestionForm
from django.views.generic.edit import FormView

def indexView(request):
    context = RequestContext(request)
    default_quiz = get_object_or_404(Quiz, name='default')
    return render(request, 'pals/index.html', {'default_quiz':default_quiz})

def palsList(request):
    pals = Pal.objects.all()
    return render(request,'pals/palsList.html',{'pals':pals})

def palProfile(request,name):
    pal = get_object_or_404(Pal,name=name)
    return render(request, 'pals/palProfile.html', {'pal':pal})

def quizView(request):
    """clean session variables and get the quiz/questions"""
    request.session.clear()
    quiz = get_object_or_404(Quiz, name='default')
    return render(request, 'pals/quiz.html', {'quiz':quiz})

def questionView(request, name):
    """first check if session is new and initialize any necessary variables, 
    then get the question and increment the counter
    """
    if 'counter' not in request.session:
        request.session['counter'] = 0
    elif request.session['done']:
        return palProfile(request, "Lydia")
    quiz = get_object_or_404(Quiz, name=name)
    counter = request.session.get('counter')
    question, done = quiz.getQuestion(counter)
    request.session['done'] = done
    form  = QuestionForm(question)
    counter += 1
    request.session['counter'] = counter
    return render(request, 'pals/question.html', {'form':form, 'quiz':quiz})

def quizTakeView(FormView):
    form_class = QuestionForm
    template_name = 'questionView.html'
