from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Scoreboard(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return self.user.user
