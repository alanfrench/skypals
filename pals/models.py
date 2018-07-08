from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Pal(models.Model):
    name = models.CharField(max_length=20)
    # 0 means they're happy criminals, 3 means they're good citizens
    morality = models.IntegerField()
    # what kind of weapons and armor they use
    profile=models.CharField(max_length=200)
    characterClass=models.CharField(max_length=100)
    classDetails = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Question(models.Model):
    # name is for reference, question_text is for display
    name = models.CharField(max_length=20)
    question_text = models.CharField(max_length=200)
    # what are we asking about?
    topic = models.CharField(max_length=100)

    def answer_question(self): # this might be handled by django forms
        # only allow answer submission if something is chosen
        # answers = self.get_answers
        # count = 0
        # for answer in answers:
        #     if answer.selected:
        #         chosen_one = answer
        #         count += 1 
        # if count != 1:
        #     pass
            # return error message and dont leave the page
        # store answer in topic of ideal_character
        return 

    def get_answers(self): # which answers are for this question?
        answers = []
        allAnswers = Answer.objects.all()
        for answer in allAnswers:
            if answer.question == self:
                answers.append(answer)
        return answers

    def get_answer_text(self):
        answers = []
        answer_objects = self.get_answers()
        for answer in answer_objects:
            answers.append(answer.answer_text)
        return answers

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    selected = False

    def __str__(self):
        return self.answer_text

# essentially a house for a list of questions
class Quiz(models.Model):
    name=models.CharField(max_length=100)
    questions=models.ManyToManyField(Question)
    slug=models.SlugField() #use slug for clean urls
    counter=0 #keeps track of the current question

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Quizzes' # or admin site says 'Quizs'

    def get_current_question(self):
        question = self.questions.all()[self.counter]
        return question

    def go_to_next_question(self):
        if self.counter >= len(self.questions.all()):
            self.counter = 0 
            return
        self.counter += 1