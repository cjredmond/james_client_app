from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import workout

class Account(models.Model):
    user = models.OneToOneField(User)
    client = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    @property
    def workout_list(self):
        print(workout.models.Workout.objects.filter(account=self))
        return self.workout_set.all()

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Account.objects.create(user=instance,client=True)
