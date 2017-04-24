from django.db import models
from user_auth.models import Account

class Workout(models.Model):
    account = models.ForeignKey(Account)
    name = models.CharField(max_length=30)
    info = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
