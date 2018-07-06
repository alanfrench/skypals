from django.test import TestCase
from .models import Pal, Question, Answer
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

def create_answer(question, answer_text):
    return Answer.objects.create(question=question, answer_text=answer_text)

class AnswerModelTests(TestCase):

    def test_can_make_answer(self):
        text = 'Are you a good citizen?'
        question = create_question('citizenship', text, 'morality')
        answer = create_answer(question, 'The best.')
        self.assertIn(answer, question.get_answers())