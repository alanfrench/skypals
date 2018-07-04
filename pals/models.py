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