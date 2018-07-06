# adapted from tomwalker on github  
# https://github.com/tomwalker/django_quiz/blob/master/quiz/forms.py
from django import forms
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                            widget=RadioSelect)