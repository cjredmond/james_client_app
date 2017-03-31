from django.db import models

class Account(models.Model):
    client = models.BooleanField(default=True)
    
