from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser
# Create your models here.

#User = get_user_model()

class Scoreboard(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    score = models.ForeignKey('self')

    def __str__(self):
        return self.user.user
    

