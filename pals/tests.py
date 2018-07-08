from django.test import TestCase
from .models import Pal, Question, Answer, Quiz
from django.urls import reverse

# Create your tests here.
def create_pal(name,morality,profile, characterClass, classDetails):
    return Pal.objects.create(name=name, morality=morality, profile=profile,
        characterClass=characterClass, classDetails=classDetails)

class PalProfileViewTests(TestCase):
    def test_can_view_pals(self):
        paleroo = create_pal('Lydia', 0, 'A nord', 'Warrior', 'combatWarrior1H')
        url = reverse('pal_profile', args=(paleroo.name,))
        response = self.client.get(url)
        self.assertContains(response, paleroo.profile)

def create_question(name, text, topic):
    return Question.objects.create(name=name, question_text=text, topic=topic)

class QuestionModelTests(TestCase):

    def test_can_make_question(self):
        text = 'Are you a good citizen?'
        question = create_question('citizenship', text, 'morality')
        self.assertIsInstance(question, Question)

    def test_get_answers_method(self):
        text = 'Are you a good citizen?'
        question = create_question('citizenship', text, 'morality')
        answer_list = []
        answer_list.append(create_answer(question, 'nah'))
        answer_list.append(create_answer(question, 'sure'))
        answers = question.get_answers()
        self.assertEqual(answers, answer_list)

    def test_get_answer_text(self):
        text = 'Are you a good citizen?'
        question = create_question('citizenship', text, 'morality')
        answer_list = []
        answer_list.append(create_answer(question, 'nah'))
        answer_list.append(create_answer(question, 'sure'))
        answers = question.get_answer_text()
        self.assertEqual(answers[0], 'nah')
        self.assertEqual(answers[1], 'sure')        

def create_answer(question, answer_text):
    return Answer.objects.create(question=question, answer_text=answer_text)

class AnswerModelTests(TestCase):

    def test_can_make_answer(self):
        text = 'Are you a good citizen?'
        question = create_question('citizenship', text, 'morality')
        answer = create_answer(question, 'The best.')
        self.assertIn(answer, question.get_answers())

def create_quiz(name, questions):
    quiz = Quiz.objects.create(name=name)
    for question in questions:
        quiz.questions.add(question)
    return quiz

def create_question_set(): # also makes their answers
        questions = []
        names = 'abc'
        answers = ['yes', 'greatsword', 'no']
        topics = ['morality', 'fighting', 'love']
        texts = ['are you a criminal?','weapon of choice?','wanna get married?']
        for i in range(3):
            q=create_question(names[i], texts[i], topics[i])
            questions.append(q)
            create_answer(q, answers[i])
        return questions

class QuizModelTests(TestCase):

    def test_can_make_quiz(self):
        questions = create_question_set()
        quizeroo = create_quiz('quizeroo', questions)
        self.assertIsInstance(quizeroo, Quiz)
        self.assertIsInstance(quizeroo.questions.all()[0], Question) 

    def test_get_current_question_method(self):
        if len(Question.objects.all()) == 0:
            create_question_set() 
        
        questions = Question.objects.all()
        quizerooni = create_quiz('quizerooni', questions)
        self.assertEqual(questions[0], quizerooni.get_current_question())
        quizerooni.go_to_next_question()
        self.assertEqual(questions[1], quizerooni.get_current_question())