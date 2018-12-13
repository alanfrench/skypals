from django.shortcuts import render, get_object_or_404
from .models import Pal, Quiz, Question, Answer
from django.template import RequestContext
# stuff for forms
from .forms import QuestionForm
from django.views.generic.edit import FormView

ANSWER_SET = Answer.objects.all()

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
    new_session(request)
    quiz = get_object_or_404(Quiz, name='default')
    return render(request, 'pals/quiz.html', {'quiz':quiz})

def questionView(request, name):
    """first check if session is new and initialize any necessary variables, 
    then get the question and increment the counter
    """

    if request.session['done']:
        palName = getPal(request)
        return palProfile(request, palName)

    quiz = get_object_or_404(Quiz, name=name)
    counter = request.session.get('counter')
    question, done = quiz.getQuestion(counter)
    # set the appropriate parameter in the session
    if request.method == 'POST':
        answerIndex = request.POST.get('answers')
        answer = ANSWER_SET.get(id=answerIndex)
        print(answer)
        print(answer.get_field())
        setParameter(request, question.get_topic(), answer.get_field())
        print(request.session.items())

    request.session['done'] = done
    form  = QuestionForm(question)
    counter += 1
    request.session['counter'] = counter
    return render(request, 'pals/question.html', {'form':form, 'quiz':quiz})

def getPal(request):
    """get ideal pal as defined by the current session and find which pal
    in the total list of pals matches the criteria best
    """
    palName = "Lydia"
    return palName


def new_session(request):
    request.session.clear()
    request.session['counter'] = 0
    request.session['done'] = False
    request.session['previous_question'] = None

def setParameter(request, field, value):
    request.session[field] = value