from rest_framework import serializers

from Treasure_Hunt_game.Game.models import Puzzle

class PuzzleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Puzzle
        fields="__all__"