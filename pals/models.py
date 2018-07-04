from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Follower(models.Model):
    name = models.CharField(max_length=20)
    moralError = "morality must be a number from 0 to 3"
    # 0 means they're happy criminals, 3 means they're good citizens
    morality = models.IntegerField(
        MinValueValidator(0, message=moralError),
        MaxValueValidator(3,message=moralError))
    # what kind of weapons and armor they use
    profile=models.CharField(max_length=100)
    fightingClass=models.CharField(max_length=100)
    # # Enable these when everything else is functional
    # # what is they're level cap
    # maxLevel=models.IntegerField()
    # lightArmor=models.IntegerField()
    # heavyArmor=models.IntegerField()
    # block=models.IntegerField()
    # oneHanded=models.IntegerField()
    # twoHanded=models.IntegerField()
    # archery=models.IntegerField()
    # lockpicking=models.IntegerField()
    # pickpocket=models.IntegerField()
    # sneak=models.IntegerField()
    # destruction=models.IntegerField()
    # restoration=models.IntegerField()
    # conjuration=models.IntegerField()
    # alteration=models.IntegerField()
    # illusion=models.IntegerField()
    # smithing=models.IntegerField()
    # alchemy=models.IntegerField()
    # enchanting=models.IntegerField()
    # speech=models.IntegerField()
    # HP=models.IntegerField() # health points
    # MP=models.IntegerField() # mana points
    # stamina=models.IntegerField()

    def __str__(self):
        return self.name