from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser
import uuid
from PIL import Image
# Create your models here.

#User = get_user_model()

class Scoreboard(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    email = models.EmailField( max_length=254)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

class BaseModel(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)

    class Meta:
        abstract = True

class Puzzle_status(BaseModel):
    clues_number = models.IntegerField(default=5)
    answer_number = models.IntegerField(default=1)
    number_of_dead_ends = models.IntegerField(default=2)

class Puzzle(BaseModel):
    question = models.CharField(max_length=200)
    image = models.ImageField(upload_to="Images")
    def Getsolution(self):
        ans_obj = Answer.objects.filter(question=self)
        data = []
        for ans in ans_obj:
            data.append({
                'answer':ans.answer_given
            })
        return data
    
    def GetClues(self):
        clues_obj = Clues.objects.filter(question = self)
        clues = []
        for c in clues_obj:
            clues.append({
                'clue1':c.clue1,
                'clue2':c.clue2
            })
        return clues



class Answer(BaseModel):
    question = models.ForeignKey(Puzzle,on_delete=models.CASCADE,)
    answer_given = models.CharField(max_length=200)


class Clues(BaseModel):
    question = models.ForeignKey(Puzzle,on_delete=models.CASCADE)
    clue1 = models.CharField(max_length=300,default="Here is the first clue")
    clue2 = models.CharField(max_length=300,default="Here is the second clue")
