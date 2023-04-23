from django.contrib import admin
from .models import Scoreboard,Puzzle,Puzzle_status,Answer,Clues
# Register your models here.


admin.site.register(Scoreboard)
admin.site.register(Puzzle)
admin.site.register(Puzzle_status)
admin.site.register(Answer)
admin.site.register(Clues)