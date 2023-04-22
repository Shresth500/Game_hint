from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser
from django.forms import PasswordInput
# Create your models here.

#User = get_user_model()

class Scoreboard(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user

    

