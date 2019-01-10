from django.shortcuts import render, get_object_or_404
from .models import Pal, Quiz, Question, Answer
from django.template import RequestContext
# stuff for forms
from .forms import QuestionForm
from django.views.generic.edit import FormView

ANSWER_SET = Answer.objects.all()
PAL_SET = Pal.objects.all()
DEBUG = True

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
    quiz = get_object_or_404(Quiz, name=name)
    counter = request.session.get('counter')
    question= quiz.getQuestion(counter)

    if DEBUG:
        print("question number " + str(counter) + ": ")
        print(question)
    # set the appropriate parameter in the session
    if request.method == 'POST':
        answerIndex = request.POST.get('answers')
        answer = ANSWER_SET.get(id=answerIndex)
        if DEBUG:
            print(answer)
            print(answer.get_field())
        setParameter(request, question.get_topic(), answer.get_field())
        if DEBUG: 
            print(request.session.items())
        counter += 1
        if quiz.noMoreQuestions(counter):
            palName = getPal(request)
            return palProfile(request, palName)
        request.session['counter'] = counter
        question = quiz.getQuestion(counter)

    form  = QuestionForm(question)
    return render(request, 'pals/question.html', {'form':form, 'quiz':quiz})

def getPal(request):
    """get ideal pal as defined by the current session and find which pal
    in the total list of pals matches the criteria best
    """
    # go through all the pals and assign scores
    palDict = dict()
    for pal in PAL_SET:
        curScore = 0
        if pal.morality == request.session['morality']:
            curScore+=1
        palDict[pal.name] = curScore

    # go through the pals and return name of highest scorer
    palChosen = False
    maxScore = 0
    palFinalists = set()
    for name, score in palDict.items():
        if not palChosen:
            palChosen = True
            palFinalists.add(name)
            maxScore = score
        elif score > maxScore:
            palFinalists.clear()
            palFinalists.add(name)
            maxScore = score
        elif score == maxScore:
            palFinalists.add(name)
    chosenOne = palFinalists.pop()
    if DEBUG:
        print("The chosen one is %s with a score of %i"%(chosenOne,maxScore))
    return chosenOne




def new_session(request):
    request.session.clear()
    request.session['counter'] = 0

def setParameter(request, field, value):
    request.session[field] = value