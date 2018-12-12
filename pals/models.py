from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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

    def __str__(self):
        return self.question_text

    def get_topic(self):
        return self.topic
    
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
            answers.append(answer.get_text)
        return answers

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200) # what the answer says
    answer_field = models.CharField(max_length=30) # what the database sees

    def __str__(self):
        return self.answer_text

    def get_text(self):
        return self.answer_text

    def get_field(self):
        return self.answer_field

class Quiz(models.Model):
    name=models.CharField(max_length=100)
    questions=models.ManyToManyField(Question)
    slug=models.SlugField() #use slug for clean urls

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizzes' # or admin site says 'Quizs'

    def getQuestion(self, counter):
        """takes a counter (which item in the list we're on) and returns the
        corresponding question, as well as whether or not there are more 
        questions left
        """
        questions = list(self.questions.all())
        question = questions[counter]
        done = (counter + 1  >= len(questions))
        return question, done