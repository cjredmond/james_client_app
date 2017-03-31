from django.db import models
from user_auth.models import Account

class Workout(models.Model):
    account = models.ForeignKey(Account)
    day = models.CharField(max_length=30)

MUSCLE_GROUPS = [('q', 'quads'), ('h', 'hamstrings'), ('c', 'calves'), ('a', 'abs'),
                 ('p', 'pecs'), ('s', 'shoulders'), ('l', 'lats'), ('b', 'biceps'),
                 ('t', 'triceps'), ('m', 'mobility')]
class Exercise(models.Model):
    workout = models.ForeignKey(Workout)
    name = models.CharField()
    muscle_group = models.CharField(max_length=1,choices=MUSCLE_GROUPS)
    sets = models.CharField(max_length=10)
    reps = models.CharField(max_length=10)
    notes = models.CharField(max_length=100,null=True,Blank=True)
